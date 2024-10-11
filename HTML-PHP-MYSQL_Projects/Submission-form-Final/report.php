<?php
require_once 'dbConnect.php';

class Report {
    private $db;

    public function __construct() {
        $dbConnect = new DBConnect();
        $this->db = $dbConnect->getConnection();
    }

    public function getSubmissions($userId = null) {
        $sql = "SELECT * FROM submissions";

        if ($userId) {
            $sql .= " WHERE id = ?";
        }

        $stmt = $this->db->prepare($sql);

        if ($userId) {
            $stmt->bind_param("i", $userId);
        }

        $stmt->execute();
        $result = $stmt->get_result();

        return $result->fetch_all(MYSQLI_ASSOC);
    }
}

$report = new Report();
$userId = isset($_GET['user_id']) ? $_GET['user_id'] : null;
$submissions = $report->getSubmissions($userId);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Report Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Submission Report</h1>
        <form method="get" action="">
            <div class="form-group">
                <label for="user_id">Search by User ID:</label>
                <input type="number" name="user_id" id="user_id" placeholder="User ID">
                <button type="submit">Search</button>
            </div>
        </form>

        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Amount</th>
                        <th>Buyer</th>
                        <th>Receipt ID</th>
                        <th>Items</th>
                        <th>Buyer Email</th>
                        <th>Buyer IP</th>
                        <th>Note</th>
                        <th>City</th>
                        <th>Phone</th>
                        <th>Entry At</th>
                        <th>Entry By</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if (!empty($submissions)): ?>
                        <?php foreach (array_slice($submissions, 0, 20) as $submission): ?>
                            <tr>
                                <td><?= htmlspecialchars($submission['id']) ?></td>
                                <td><?= htmlspecialchars($submission['amount']) ?></td>
                                <td><?= htmlspecialchars($submission['buyer']) ?></td>
                                <td><?= htmlspecialchars($submission['receipt_id']) ?></td>
                                <td><?= htmlspecialchars($submission['items']) ?></td>
                                <td><?= htmlspecialchars($submission['buyer_email']) ?></td>
                                <td><?= htmlspecialchars($submission['buyer_ip']) ?></td>
                                <td><?= htmlspecialchars($submission['note']) ?></td>
                                <td><?= htmlspecialchars($submission['city']) ?></td>
                                <td><?= htmlspecialchars($submission['phone']) ?></td>
                                <td><?= htmlspecialchars($submission['entry_at']) ?></td>
                                <td><?= htmlspecialchars($submission['entry_by']) ?></td>
                            </tr>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <tr>
                            <td colspan="12">No submissions found.</td>
                        </tr>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>

        <a href="index.php" class="button">Back to Home</a>
    </div>
</body>
</html>
