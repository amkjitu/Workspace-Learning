# import cv2
# import numpy as np

# # Match your parameters EXACTLY
# squares_x = 7
# squares_y = 5
# square_len_mm = 30
# marker_len_mm = 15
# dict_name = cv2.aruco.DICT_5X5_100

# dictionary = cv2.aruco.getPredefinedDictionary(dict_name)

# if hasattr(cv2.aruco, "CharucoBoard_create"):
#     board = cv2.aruco.CharucoBoard_create(
#         squares_x, squares_y, square_len_mm, marker_len_mm, dictionary
#     )
# else:
#     board = cv2.aruco.CharucoBoard(
#         (squares_x, squares_y), square_len_mm, marker_len_mm, dictionary
#     )

# # Generate 300 DPI image (A4 size: 2480x3508 pixels)
# img = board.generateImage((2100, 1500), marginSize=20, borderBits=1)

# cv2.imwrite("charuco_board_7x5.png", img)
# print("Board saved to charuco_board_7x5.png")
# print(
#     f"This board has {squares_x * squares_y // 2} markers (IDs 0-{squares_x * squares_y // 2 - 1})"
# )


# import cv2
# import numpy as np

# '''
# py -3.10 -m calibrate_charuco_dual_shared_pose --rtsp_left "rtsp://admin:L200461B@192.168.0.182:554/cam/realmonitor?channel=1&subtype=0" --rtsp_right "rtsp://admin:L2574467@192.168.0.151:554/cam/realmonitor?channel=1&subtype=0" --squares_x 6 --squares_y 4 --square_len_mm 45 --marker_len_mm 22 --aruco_dict 4X4_50 --preview --recalibrate
# '''

# # CORRECTED parameters for your Dahua 3MP camera
# squares_x = 6
# squares_y = 4
# square_len_mm = 45  # Larger squares
# marker_len_mm = 22  # Larger markers
# dict_name = cv2.aruco.DICT_4X4_50  # Simpler dictionary

# dictionary = cv2.aruco.getPredefinedDictionary(dict_name)

# if hasattr(cv2.aruco, "CharucoBoard_create"):
#     board = cv2.aruco.CharucoBoard_create(
#         squares_x, squares_y, square_len_mm, marker_len_mm, dictionary
#     )
# else:
#     board = cv2.aruco.CharucoBoard(
#         (squares_x, squares_y), square_len_mm, marker_len_mm, dictionary
#     )

# # Generate high-res image for printing (A3 size recommended)
# img = board.generateImage((3508, 2480), marginSize=30, borderBits=1)

# cv2.imwrite("charuco_6x4_dahua.png", img)
# print(f"✓ Board saved: charuco_6x4_dahua.png")
# print(f"✓ Board has {(squares_x * squares_y) // 2} markers")
# print(
#     f"✓ Total board size: {squares_x * square_len_mm}mm x {squares_y * square_len_mm}mm"
# )
# print(f"  = {squares_x * square_len_mm / 10}cm x {squares_y * square_len_mm / 10}cm")
# print("\nPrint this on A3 paper at 100% scale (no 'fit to page')")
# print("Mount on rigid board/clipboard for flatness")


# import cv2
# import numpy as np

# # Target: A2 paper (landscape) 594 x 420 mm
# # Fit the 12x9 grid with safe margins on A2:
# squares_x = 12
# squares_y = 9
# square_len_mm = 46.0  # 12 * 46 = 552 mm  (fits within 594 mm)
# marker_len_mm = 32.0  # ~0.7 * square (robust)
# dict_name = cv2.aruco.DICT_5X5_1000

# dictionary = cv2.aruco.getPredefinedDictionary(dict_name)
# try:
#     board = cv2.aruco.CharucoBoard_create(
#         squares_x, squares_y, square_len_mm, marker_len_mm, dictionary
#     )
# except AttributeError:
#     # Older OpenCV fallback
#     board = cv2.aruco.CharucoBoard(
#         (squares_x, squares_y), square_len_mm, marker_len_mm, dictionary
#     )

# # Render at A2 @ 300 DPI → 7016 x 4961 px (landscape)
# # Add a healthy margin so the printer doesn't clip (120 px ≈ 10 mm at 300 dpi)
# canvas_px = (7016, 4961)  # (width, height)
# margin_px = 120
# border_bits = 1

# # OpenCV ArUco has both .generateImage and .draw across versions; try .generateImage first
# if hasattr(board, "generateImage"):
#     img = board.generateImage(canvas_px, marginSize=margin_px, borderBits=border_bits)
# else:
#     # Older API uses .draw(size, img, marginSize, borderBits)
#     img = board.draw(canvas_px, marginSize=margin_px, borderBits=border_bits)

# out_name = "charuco_12x9_A2_46mm_32mm_Dict5x5_1000.png"
# cv2.imwrite(out_name, img)

# # Helpful reporting
# internal_corners = (squares_x - 1) * (
#     squares_y - 1
# )  # ChArUco corners used in calibration
# board_w_mm = squares_x * square_len_mm
# board_h_mm = squares_y * square_len_mm

# print(f"✓ Board saved: {out_name}")
# print(f"✓ Grid: {squares_y} rows × {squares_x} cols")
# print(f"✓ Square: {square_len_mm} mm, Marker: {marker_len_mm} mm, Dict: 5x5_1000")
# print(
#     f"✓ Active area: {board_w_mm:.1f} mm × {board_h_mm:.1f} mm ({board_w_mm/10:.1f} cm × {board_h_mm/10:.1f} cm)"
# )
# print(f"✓ Internal ChArUco corners: {internal_corners}")
# print("\nPRINTING NOTES:")
# print("• Print on A2 paper (landscape) at 100% scale (no 'fit to page').")
# print(
#     "• Use matte paper/board; keep it flat. Verify one square = 46.0 mm with a ruler."
# )
# print(
#     "• If your printer requires larger margins, reduce square_len_mm to 45.5 mm and re-run."
# )


import cv2
import numpy as np

# A3 paper (landscape): 420 x 297 mm  → 4961 x 3508 px @ 300 dpi
squares_x = 12  # columns (wide)
squares_y = 9  # rows (tall)
square_len_mm = 31.0  # 12 * 31 = 372 mm width; 9 * 31 = 279 mm height
marker_len_mm = 22.0  # ~0.71 * square (robust)
dict_name = cv2.aruco.DICT_5X5_1000

dictionary = cv2.aruco.getPredefinedDictionary(dict_name)
try:
    board = cv2.aruco.CharucoBoard_create(
        squares_x, squares_y, square_len_mm, marker_len_mm, dictionary
    )
except AttributeError:
    board = cv2.aruco.CharucoBoard(
        (squares_x, squares_y), square_len_mm, marker_len_mm, dictionary
    )

canvas_px = (4961, 3508)  # width, height (A3 landscape @ 300 dpi)
margin_px = 120  # ≈10 mm; increases print safety
border_bits = 1

if hasattr(board, "generateImage"):
    img = board.generateImage(canvas_px, marginSize=margin_px, borderBits=border_bits)
else:
    img = board.draw(canvas_px, marginSize=margin_px, borderBits=border_bits)

out_name = "charuco_12x9_A3_31mm_22mm_Dict5x5_1000.png"
cv2.imwrite(out_name, img)

internal_corners = (squares_x - 1) * (squares_y - 1)  # 11 * 8 = 88
board_w_mm = squares_x * square_len_mm  # 372 mm
board_h_mm = squares_y * square_len_mm  # 279 mm

print(f"✓ Board saved: {out_name}")
print(f"✓ Grid: {squares_y} rows × {squares_x} cols")
print(f"✓ Square: {square_len_mm} mm, Marker: {marker_len_mm} mm, Dict: 5x5_1000")
print(f"✓ Active area: {board_w_mm:.1f} mm × {board_h_mm:.1f} mm")
print(f"✓ Internal ChArUco corners: {internal_corners}")
print("\nPRINTING NOTES:")
print("• Print on A3 (landscape) at 100% scale (disable 'fit to page').")
print("• Use matte paper/foam board; keep it flat.")
print("• Verify one square = 31.0 mm with a ruler before shooting.")
