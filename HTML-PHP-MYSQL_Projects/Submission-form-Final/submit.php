<?php
require_once 'dbConnect.php';

class Submission {
    private $db;

    public function __construct() {
        $dbConnect = new DBConnect();
        $this->db = $dbConnect->getConnection();
    }

    public function validateInput($data) {
        $errors = [];

        // Validation rules
        if (!filter_var($data['amount'], FILTER_VALIDATE_INT)) {
            $errors['amount'] = "Amount must be a number.";
        }
        if (!preg_match('/^[a-zA-Z0-9 ]{1,20}$/', $data['buyer'])) {
            $errors['buyer'] = "Buyer name should contain only text, spaces, and numbers, and not exceed 20 characters.";
        }
        if (empty($data['receipt_id']) || preg_match('/\s/', $data['receipt_id'])) {
            $errors['receipt_id'] = "Receipt ID must not contain spaces and cannot be empty.";
        }
        if (empty($data['items'])) {
            $errors['items'] = "Items field cannot be empty.";
        }
        if (!filter_var($data['buyer_email'], FILTER_VALIDATE_EMAIL)) {
            $errors['buyer_email'] = "Invalid email format.";
        }
        if (str_word_count($data['note']) > 30) {
            $errors['note'] = "Note cannot exceed 30 words.";
        }
        if (!preg_match('/^[a-zA-Z ]+$/', $data['city'])) {
            $errors['city'] = "City should contain only text and spaces.";
        }
        if (!preg_match('/^[0-9]+$/', $data['phone'])) {
            $errors['phone'] = "Phone should contain only numbers.";
        }
        if (!filter_var($data['entry_by'], FILTER_VALIDATE_INT)) {
            $errors['entry_by'] = "Entry by must be a number.";
        }

        return $errors;
    }

    public function saveSubmission($data) {
        $stmt = $this->db->prepare("INSERT INTO submissions (amount, buyer, receipt_id, items, buyer_email, buyer_ip, note, city, phone, entry_at, entry_by) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, NOW(), ?)");

        // Fetching user's IP
        $buyer_ip = $_SERVER['REMOTE_ADDR'];

        // Bind parameters
        $stmt->bind_param("issssssssi", 
            $data['amount'], 
            $data['buyer'], 
            $data['receipt_id'], 
            $data['items'], 
            $data['buyer_email'], 
            $buyer_ip, 
            $data['note'], 
            $data['city'], 
            $data['phone'], 
            $data['entry_by']
        );

        if ($stmt->execute()) {
            return "Submission successful!";
        } else {
            return "Error: " . $stmt->error;
        }

        $stmt->close();
    }
}

// Handling the form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $submission = new Submission();
    $data = $_POST;

    // Validate input
    $errors = $submission->validateInput($data);

    if (empty($errors)) {
        // Save submission
        $success=$submission->saveSubmission($data);
        //echo "<p>$success</p>"; // a success message
        // Redirect to report page after successful submission
        header('Location: report.php');
        exit(); // Ensure script stops executing after redirect
    } else {
        foreach ($errors as $error) {
            echo "<p>Error: $error</p>";
        }
    }
}
?>
