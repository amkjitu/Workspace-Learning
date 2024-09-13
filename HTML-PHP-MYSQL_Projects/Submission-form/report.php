<?php

class Report {
    private $db;

    public function __construct() {
        // Database connection
        $this->db = new mysqli('localhost', 'root', '', 'auditors');

        if ($this->db->connect_error) {
            die("Connection failed: " . $this->db->connect_error);
        }
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
    <title>Report</title>
</head>
<body>
    <form method="get" action="">
        <label for="user_id">Search by User ID:</label>
        <input type="number" name="user_id" id="user_id">
        <button type="submit">Search</button>
    </form>

    <h2>Submissions</h2>
    <table border="1">
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
        <?php foreach ($submissions as $submission): ?>
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
    </table>
</body>
</html>
