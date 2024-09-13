<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditor's Operation</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            background-color: #FFEAEA;  
        }
        h2 {
            color: #000;
            text-align: center;
            margin-top: -20px;
        }
        table {
            background-color: #DAFFC8;
            box-shadow: 0 0 15px rgba(255, 150, 0, 0.3);
        }
        th {
            /**background-color: #007bff;**/
            color: #ffffff;
        }
    
        td, th {
            text-align: center;
            vertical-align: middle;
            font-size: larger;
        }
        .rectangular-input {
            border-radius: 0;
        }
        .btn-success {
            background-color: #28a745;
            border-color: #28a745;
        }
        .btn-success:hover {
            background-color: #218838;
            border-color: #1e7e34;
        }
        .browser {
            background: white;
        }
        footer {
            text-align: center;
            background-color: DarkSalmon;
            color: white;
        }
    </style>
</head>
<body>
    <?php
    $ac_no = isset($_GET['ac_no']) ? $_GET['ac_no'] : '';
    $sign_status = isset($_GET['sign_status']) ? $_GET['sign_status'] : '';
    $sign_remarks = isset($_GET['sign_remarks']) ? $_GET['sign_remarks'] : '';
    $sign_risk_grade = isset($_GET['sign_risk_grade']) ? $_GET['sign_risk_grade'] : '';
    $kyc_status = isset($_GET['kyc_status']) ? $_GET['kyc_status'] : '';
    $kyc_remarks = isset($_GET['kyc_remarks']) ? $_GET['kyc_remarks'] : '';
    $kyc_risk_grade = isset($_GET['kyc_risk_grade']) ? $_GET['kyc_risk_grade'] : '';
    $ces_status = isset($_GET['ces_status']) ? $_GET['ces_status'] : '';
    $ces_remarks = isset($_GET['ces_remarks']) ? $_GET['ces_remarks'] : '';
    $ces_risk_grade = isset($_GET['ces_risk_grade']) ? $_GET['ces_risk_grade'] : '';
    ?>
    <div class="container mt-5">
        <h2>Basic Input by Auditors</h2>
        <form id="audit_inputForm" action="process.php" method="post">
            <table class="table table-bordered">
                <thead style="background-color: #581845;">
                    <tr>
                        <th colspan="1">A/C No:</th>
                        <th colspan="2">
                            <input type="text" class="form-control rectangular-input" id="ac_no" name="ac_no" placeholder="Input Box" value="<?php echo htmlspecialchars($ac_no); ?>" required>
                        </th>
                        <th colspan="1">
                            <button type="button" class="btn btn-primary" name="action" value="search" onclick="setRequired('search')" style="width: 100%; border-radius:0;">
                                <span class="bi-search"></span>&nbsp;Search
                            </button>
                        </th>
                        <th colspan="1">
                            <button type="button" class="btn btn-info" name="action" value="view" onclick="setRequired('view')" style="width: 100%; border-radius:0;"><span class="bi-table"></span>&nbsp;View Data Table
                            </button>
                        </th>
                    </tr>
                </thead>

                <thead style="background-color: #00094B;">
                    <tr>
                        <th>Serial No</th>
                        <th>Name</th>
                        <th>Status</th>
                        <th>Remarks</th>
                        <th>Risk Grade</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Signature</td>
                        <td>
                            <select class="form-control" id="sign_status" name="sign_status">
                                <option value="" disabled <?php echo $sign_status == '' ? 'selected' : ''; ?>>-Select-</option>
                                <option value="Found" <?php echo $sign_status == 'Found' ? 'selected' : ''; ?>>Found</option>
                                <option value="Not_Found" <?php echo $sign_status == 'Not_Found' ? 'selected' : ''; ?>>Not Found</option>
                            </select>
                        </td>
                        <td>
                            <textarea class="form-control" id="sign_remarks" name="sign_remarks" rows="2"><?php echo htmlspecialchars($sign_remarks); ?></textarea>
                        </td>
                        <td>
                            <select class="form-control" id="sign_risk_grade" name="sign_risk_grade">
                                <option value="" disabled <?php echo $sign_risk_grade == '' ? 'selected' : ''; ?>>-Select-</option>
                                <option value="High" <?php echo $sign_risk_grade == 'High' ? 'selected' : ''; ?>>High</option>
                                <option value="Medium" <?php echo $sign_risk_grade == 'Medium' ? 'selected' : ''; ?>>Medium</option>
                                <option value="Low" <?php echo $sign_risk_grade == 'Low' ? 'selected' : ''; ?>>Low</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>KYC</td>
                        <td>
                            <select class="form-control" id="kyc_status" name="kyc_status">
                                <option value="" disabled <?php echo $kyc_status == '' ? 'selected' : ''; ?>>-Select-</option>
                                <option value="Found" <?php echo $kyc_status == 'Found' ? 'selected' : ''; ?>>Found</option>
                                <option value="Not_Found" <?php echo $kyc_status == 'Not_Found' ? 'selected' : ''; ?>>Not Found</option>
                            </select>
                        </td>
                        <td>
                            <textarea class="form-control" id="kyc_remarks" name="kyc_remarks" rows="2"><?php echo htmlspecialchars($kyc_remarks); ?></textarea>
                        </td>
                        <td>
                            <select class="form-control" id="kyc_risk_grade" name="kyc_risk_grade">
                                <option value="" disabled <?php echo $kyc_risk_grade == '' ? 'selected' : ''; ?>>-Select-</option>
                                <option value="High" <?php echo $kyc_risk_grade == 'High' ? 'selected' : ''; ?>>High</option>
                                <option value="Medium" <?php echo $kyc_risk_grade == 'Medium' ? 'selected' : ''; ?>>Medium</option>
                                <option value="Low" <?php echo $kyc_risk_grade == 'Low' ? 'selected' : ''; ?>>Low</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>CES</td>
                        <td>
                            <select class="form-control" id="ces_status" name="ces_status">
                                <option value="" disabled <?php echo $ces_status == '' ? 'selected' : ''; ?>>-Select-</option>
                                <option value="Found" <?php echo $ces_status == 'Found' ? 'selected' : ''; ?>>Found</option>
                                <option value="Not_Found" <?php echo $ces_status == 'Not_Found' ? 'selected' : ''; ?>>Not Found</option>
                            </select>
                        </td>
                        <td>
                            <textarea class="form-control" id="ces_remarks" name="ces_remarks" rows="2"><?php echo htmlspecialchars($ces_remarks); ?></textarea>
                        </td>
                        <td>
                            <select class="form-control" id="ces_risk_grade" name="ces_risk_grade">
                                <option value="" disabled <?php echo $ces_risk_grade == '' ? 'selected' : ''; ?>>-Select-</option>
                                <option value="High" <?php echo $ces_risk_grade == 'High' ? 'selected' : ''; ?>>High</option>
                                <option value="Medium" <?php echo $ces_risk_grade == 'Medium' ? 'selected' : ''; ?>>Medium</option>
                                <option value="Low" <?php echo $ces_risk_grade == 'Low' ? 'selected' : ''; ?>>Low</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2" class="text-center">
                            <button type="submit" name="action" value="update" onclick="setRequired('update')" class="btn btn-warning btn-lg" style="width: 100%;">Update</button>
                        </td>
                        <td colspan="2" class="text-center">
                            <button type="submit" name="action" value="create" onclick="setRequired('submit')" class="btn btn-success btn-lg" style="width: 100%;">Submit</button>
                        </td>  
                        <td colspan="2" class="text-center">    
                            <button type="button" id="delete_data" class="btn btn-danger btn-lg" style="width: 100%; " onclick="setRequired('delete')">Delete</button>
                        </td>
                    </tr>

                    <!--
                    ///vertical buttons
                    <tr>
                        <td colspan="3" class="text-center">
                            <button type="submit" name="action" value="create" onclick="setRequired('submit')" class="btn btn-success btn-lg" style="width: 100%; border-radius: 0;">Submit</button>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="3" class="text-center">
                            <button type="submit" name="action" value="update" onclick="setRequired('update')" class="btn btn-warning btn-lg" style="width: 100%; border-radius: 0;">Update</button>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="3" class="text-center">
                            <button type="button" id="delete_data" class="btn btn-danger btn-lg" style="width: 100%; border-radius: 0;" onclick="setRequired('delete')">Delete</button>
                        </td>
                    </tr>
                    -->

                </tbody>
            </table>
        </form>
    </div>

    <!-- View Results Modal -->
    <div class="modal fade" id="viewResultsModal" tabindex="-1" role="dialog" aria-labelledby="viewResultsModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="viewResultsModalLabel">Data Table</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="table-responsive">
                        <table class="table table-striped table-hover">
                            <thead class="thead-dark">
                                <tr>
                                    <th scope="col">A/C No.</th>
                                    <th scope="col">Sign Status</th>
                                    <th scope="col">Sign Remarks</th>
                                    <th scope="col">Sign Risk Grade</th>
                                    <th scope="col">KYC Status</th>
                                    <th scope="col">KYC Remarks</th>
                                    <th scope="col">KYC Risk Grade</th>
                                    <th scope="col">CES Status</th>
                                    <th scope="col">CES Remarks</th>
                                    <th scope="col">CES Risk Grade</th>
                                </tr>
                            </thead>
                            <tbody id="viewResultsBody">
                                <!-- Search results will be inserted here by JavaScript -->
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="deleteModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="deleteModalLabel">Alert!</h5>
                </div>
                <div class="modal-body">
                    <p>Are you sure you want to delete?</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" onclick="confirmDelete()">Delete</button>
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Submitted Modal -->
    <div class="modal fade" id="submittedModal" tabindex="-1" role="dialog" aria-labelledby="submittedModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="submittedModalLabel">Success</h5>
                </div>
                <div class="modal-body">
                    <p>Submitted successfully!</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Updated Modal -->
    <div class="modal fade" id="updatedModal" tabindex="-1" role="dialog" aria-labelledby="updatedModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="updatedModalLabel">Success</h5>
                </div>
                <div class="modal-body">
                    <p>Updated successfully!</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Duplicate Data Found Modal -->
    <div class="modal fade" id="duplicateDataModal" tabindex="-1" role="dialog" aria-labelledby="duplicateDataModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="duplicateDataModalLabel">Info</h5>
                </div>
                <div class="modal-body">
                    <p> 
                    A/C No: <b><?php echo htmlspecialchars($ac_no);?> </b> already exists. 
                    </p>
                    
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <!-- No Data Found Modal -->
    <div class="modal fade" id="noDataModal" tabindex="-1" role="dialog" aria-labelledby="noDataModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="noDataModalLabel">Info</h5>
                </div>
                <div class="modal-body">
                    <p>No data found for the given A/C No.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

    <script>
        function setRequired(action) {
            var ac_no = document.getElementById('ac_no');
            var ac_no_value = document.getElementById('ac_no').value;
            var sign_status = document.getElementById('sign_status');
            var sign_remarks = document.getElementById('sign_remarks');
            var sign_risk_grade = document.getElementById('sign_risk_grade');

            var kyc_status = document.getElementById('kyc_status');
            var kyc_remarks = document.getElementById('kyc_remarks');
            var kyc_risk_grade = document.getElementById('kyc_risk_grade');

            var ces_status = document.getElementById('ces_status');
            var ces_remarks = document.getElementById('ces_remarks');
            var ces_risk_grade = document.getElementById('ces_risk_grade');


            // Clear required attribute on both fields initially
            ac_no.removeAttribute('required');
            sign_status.removeAttribute('required');
            sign_remarks.removeAttribute('required');
            sign_risk_grade.removeAttribute('required');

            kyc_status.removeAttribute('required');
            kyc_remarks.removeAttribute('required');
            kyc_risk_grade.removeAttribute('required');

            ces_status.removeAttribute('required');
            ces_remarks.removeAttribute('required');
            ces_risk_grade.removeAttribute('required');


            if (action === 'delete' && ac_no_value !== "") {
                $('#deleteModal').modal('show');
            } else if (action === 'delete') {
                alert('A/C No is required to delete.');
            } else if (action === 'submit') {
                ac_no.setAttribute('required', 'required');
                sign_status.setAttribute('required', 'required');
                sign_remarks.setAttribute('required', 'required');
                sign_risk_grade.setAttribute('required', 'required');

                kyc_status.setAttribute('required', 'required');
                kyc_remarks.setAttribute('required', 'required');
                kyc_risk_grade.setAttribute('required', 'required');

                ces_status.setAttribute('required', 'required');
                ces_remarks.setAttribute('required', 'required');
                ces_risk_grade.setAttribute('required', 'required');

                document.getElementById('audit_inputForm').action = 'process.php?action=submit';
            } else if (action === 'update') {
                ac_no.setAttribute('required', 'required');
                sign_status.setAttribute('required', 'required');
                sign_remarks.setAttribute('required', 'required');
                sign_risk_grade.setAttribute('required', 'required');

                kyc_status.setAttribute('required', 'required');
                kyc_remarks.setAttribute('required', 'required');
                kyc_risk_grade.setAttribute('required', 'required');

                ces_status.setAttribute('required', 'required');
                ces_remarks.setAttribute('required', 'required');
                ces_risk_grade.setAttribute('required', 'required');

                document.getElementById('audit_inputForm').action = 'process.php?action=update';
            } else if (action === 'search' && ac_no_value !== "") { 
                document.getElementById('audit_inputForm').action = 'process.php?action=search';
                document.getElementById('audit_inputForm').submit();
            }
            else if (action === 'search') { 
                ac_no.setAttribute('required', 'required');
            }else if (action === 'view') { 
                document.getElementById('audit_inputForm').action = 'process.php?action=view';
                document.getElementById('audit_inputForm').submit();
            }
            
            document.getElementById('audit_inputForm').reportValidity();
        }

        function confirmDelete() {
            const form = document.getElementById('audit_inputForm');
            form.action = 'process.php?action=delete';
            form.submit();
        }

        function showModal(modalId) {
            $('#' + modalId).modal('show');
        }

        function closeModal(modalId) {
            $('#' + modalId).modal('hide');
            window.location.href = window.location.href; // Redirect to the same page
        }

        // Handle form submission responses
        $(document).ready(function() {
            const urlParams = new URLSearchParams(window.location.search);
            const action = urlParams.get('action');
            if (action === 'submit') {
                showModal('submittedModal');
            } 
            else if (action === 'update') {
                showModal('updatedModal');
            } 
            else if (action === 'view' && urlParams.has('view_table')) {
                var viewTable = JSON.parse(decodeURIComponent(urlParams.get('view_table')));
                var tableBody = $('#viewResultsBody');
                tableBody.empty();
                viewTable.forEach(function(row) {
                    var tr = $('<tr></tr>');
                    tr.append('<td>' + row.ac_no + '</td>');
                    tr.append('<td>' + row.sign_status + '</td>');
                    tr.append('<td>' + row.sign_remarks + '</td>');
                    tr.append('<td>' + row.sign_risk_grade + '</td>');
                    tr.append('<td>' + row.kyc_status + '</td>');
                    tr.append('<td>' + row.kyc_remarks + '</td>');
                    tr.append('<td>' + row.kyc_risk_grade + '</td>');
                    tr.append('<td>' + row.ces_status + '</td>');
                    tr.append('<td>' + row.ces_remarks + '</td>');
                    tr.append('<td>' + row.ces_risk_grade + '</td>');
                    tableBody.append(tr);
                });
                $('#viewResultsModal').modal('show');
            }
            else if (action === 'duplicateData') {
                showModal('duplicateDataModal');
            } 
            else if (action === 'noData') {
                showModal('noDataModal');
            }
            
        });
    </script>

</body>

<footer>
  <p>Developed by Ayrin. 2024</p>
</footer>
</html>
