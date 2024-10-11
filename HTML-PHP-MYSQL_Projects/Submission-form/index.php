<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Submission Form</title>
</head>
<body>
    <form action="submit.php" method="post">
        <label for="amount">Amount:</label>
        <input type="number" name="amount" id="amount" required><br>
        
        <label for="buyer">Buyer:</label>
        <input type="text" name="buyer" id="buyer" maxlength="20" required><br>
        
        <label for="receipt_id">Receipt ID:</label>
        <input type="text" name="receipt_id" id="receipt_id" required><br>
        
        <label for="items">Items:</label>
        <input type="text" name="items" id="items" required><br>
        
        <label for="buyer_email">Buyer Email:</label>
        <input type="email" name="buyer_email" id="buyer_email" required><br>
        
        <label for="note">Note:</label>
        <textarea name="note" id="note" maxlength="200" required></textarea><br>
        
        <label for="city">City:</label>
        <input type="text" name="city" id="city" required><br>
        
        <label for="phone">Phone:</label>
        <input type="text" name="phone" id="phone" required><br>
        
        <label for="entry_by">Entry By:</label>
        <input type="number" name="entry_by" id="entry_by" required><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
