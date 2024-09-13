<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $action = $_GET['action'];
    $ac_no = $_POST['ac_no'];
    $sign_status = $_POST['sign_status'];
    $sign_remarks = $_POST['sign_remarks'];
    $sign_risk_grade = $_POST['sign_risk_grade'];
    $kyc_status = $_POST['kyc_status'];
    $kyc_remarks = $_POST['kyc_remarks'];
    $kyc_risk_grade = $_POST['kyc_risk_grade'];
    $ces_status = $_POST['ces_status'];
    $ces_remarks = $_POST['ces_remarks'];
    $ces_risk_grade = $_POST['ces_risk_grade'];

    // Database connection
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "auditors";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if ($action == 'submit') {
        // Handle submit action
        $sql = "INSERT INTO auditor_inputs (ac_no, sign_status, sign_remarks, sign_risk_grade, kyc_status, kyc_remarks, kyc_risk_grade, ces_status, ces_remarks, ces_risk_grade)
                VALUES ('$ac_no', '$sign_status', '$sign_remarks', '$sign_risk_grade', '$kyc_status', '$kyc_remarks', '$kyc_risk_grade', '$ces_status', '$ces_remarks', '$ces_risk_grade')";
        if ($conn->query($sql) === TRUE) {
            header("Location: index.php?action=submit");
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    } elseif ($action == 'update') {
        // Handle update action
        $sql = "UPDATE auditor_inputs SET sign_status='$sign_status', sign_remarks='$sign_remarks', sign_risk_grade='$sign_risk_grade',
                kyc_status='$kyc_status', kyc_remarks='$kyc_remarks', kyc_risk_grade='$kyc_risk_grade',
                ces_status='$ces_status', ces_remarks='$ces_remarks', ces_risk_grade='$ces_risk_grade'
                WHERE ac_no='$ac_no'";
        if ($conn->query($sql) === TRUE) {
            header("Location: index.php?action=update");
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    } elseif ($action == 'delete') {
        // Check if the account exists
        $check_sql = "SELECT * FROM auditor_inputs WHERE ac_no='$ac_no'";
        $result = $conn->query($check_sql);
        if ($result->num_rows > 0) {
            $sql = "DELETE FROM auditor_inputs WHERE ac_no='$ac_no'";
            if ($conn->query($sql) === TRUE) {
                header("Location: index.php?action=delete");
            } else {
                echo "Error deleting record: " . $conn->error;
            }
        } else {
            header("Location: index.php?action=noData");
        }
    } elseif ($action == 'search') {
        $sql = "SELECT * FROM auditor_inputs WHERE ac_no='$ac_no'";
        $result = $conn->query($sql);
        if ($result->num_rows > 0) {
            echo "<table class='table table-bordered'>
                    <thead>
                        <tr>
                            <th>A/C No.</th>
                            <th>Signature</th>
                            <th>Sign Status</th>
                            <th>Sign Remarks</th>
                            <th>Sign Risk Grade</th>
                            <th>KYC</th>
                            <th>KYC Status</th>
                            <th>KYC Remarks</th>
                            <th>KYC Risk Grade</th>
                            <th>CES</th>
                            <th>CES Status</th>
                            <th>CES Remarks</th>
                            <th>CES Risk Grade</th>
                        </tr>
                    </thead>
                    <tbody>";
            while($row = $result->fetch_assoc()) {
                echo "<tr>
                        <td>" . $row["ac_no"]. "</td>
                        <td>" . $row["sign_status"]. "</td>
                        <td>" . $row["sign_remarks"]. "</td>
                        <td>" . $row["sign_risk_grade"]. "</td>
                        <td>" . $row["kyc_status"]. "</td>
                        <td>" . $row["kyc_remarks"]. "</td>
                        <td>" . $row["kyc_risk_grade"]. "</td>
                        <td>" . $row["ces_status"]. "</td>
                        <td>" . $row["ces_remarks"]. "</td>
                        <td>" . $row["ces_risk_grade"]. "</td>
                    </tr>";
            }
            echo "</tbody></table>";
        } else {
            header("Location: index.php?action=noData");
        }
    }

    $conn->close();
}
?>
