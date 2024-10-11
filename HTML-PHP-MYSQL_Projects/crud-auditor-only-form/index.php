<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD Operations with Confirmation Modals</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        h2 {
            color: #000;
            text-align: center;
            margin-top: -48px;
        }
        table {
            background-color: #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        th {
            background-color: #007bff;
            color: #ffffff;
        }
        td, th {
            text-align: center;
            vertical-align: middle;
            font-size: larger;
        }
        .btn-success {
            background-color: #28a745;
            border-color: #28a745;
        }
        .btn-success:hover {
            background-color: #218838;
            border-color: #1e7e34;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h2>Basic Input by Auditors</h2>
        <form id="audit_inputForm" action="process.php" method="post">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th colspan="1">A/C No:</th>
                        <th colspan="3">
                            <input type="text" class="form-control" id="ac_no" name="ac_no" placeholder="Input Box" required>
                        </th>
                        <th colspan="1">
                            <button type="button" class="btn btn-secondary" name="action" value="search" onclick="setRequired('search')" style="width: 100%; border-radius:0;">
                                <span class="bi-search"></span>&nbsp;Search
                            </button>
                        </th>
                    </tr>
                </thead>
                <thead>
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
                                <option value="" disabled selected>-Select-</option>
                                <option value="Found">Found</option>
                                <option value="Not_Found">Not Found</option>
                            </select>
                        </td>
                        <td>
                            <textarea class="form-control" id="sign_remarks" name="sign_remarks" rows="2"></textarea>
                        </td>
                        <td>
                            <select class="form-control" id="sign_risk_grade" name="sign_risk_grade">
                                <option value="" disabled selected>-Select-</option>
                                <option value="High">High</option>
                                <option value="Medium">Medium</option>
                                <option value="Low">Low</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>KYC</td>
                        <td>
                            <select class="form-control" id="kyc_status" name="kyc_status">
                                <option value="" disabled selected>-Select-</option>
                                <option value="Found">Found</option>
                                <option value="Not_Found">Not Found</option>
                            </select>
                        </td>
                        <td>
                            <textarea class="form-control" id="kyc_remarks" name="kyc_remarks" rows="2"></textarea>
                        </td>
                        <td>
                            <select class="form-control" id="kyc_risk_grade" name="kyc_risk_grade">
                                <option value="" disabled selected>-Select-</option>
                                <option value="High">High</option>
                                <option value="Medium">Medium</option>
                                <option value="Low">Low</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>CES</td>
                        <td>
                            <select class="form-control" id="ces_status" name="ces_status">
                                <option value="" disabled selected>-Select-</option>
                                <option value="Found">Found</option>
                                <option value="Not_Found">Not Found</option>
                            </select>
                        </td>
                        <td>
                            <textarea class="form-control" id="ces_remarks" name="ces_remarks" rows="2"></textarea>
                        </td>
                        <td>
                            <select class="form-control" id="ces_risk_grade" name="ces_risk_grade">
                                <option value="" disabled selected>-Select-</option>
                                <option value="High">High</option>
                                <option value="Medium">Medium</option>
                                <option value="Low">Low</option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="5" class="text-center">
                            <button type="submit" name="action" value="create" onclick="setRequired('submit')" class="btn btn-success btn-lg" style="width: 100%; border-radius: 0;">Submit</button>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="5" class="text-center">
                            <button type="submit" name="action" value="update" onclick="setRequired('update')" class="btn btn-warning btn-lg" style="width: 100%; border-radius: 0;">Update</button>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="5" class="text-center">
                            <button type="button" id="delete_data" class="btn btn-danger btn-lg" style="width: 100%; border-radius: 0;" onclick="setRequired('delete')">Delete</button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </form>
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
            //else if (action === 'delete') {
                //showModal('deleteModal');
            //} 
            else if (action === 'noData') {
                showModal('noDataModal');
            }
        });
    </script>

</body>
</html>
