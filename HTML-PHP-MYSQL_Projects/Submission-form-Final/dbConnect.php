<?php

class DBConnect {
    private $host = 'localhost';
    private $username = 'root';
    private $password = '';
    private $database = 'auditors';
    protected $db;

    public function __construct() {
        $this->db = new mysqli($this->host, $this->username, $this->password, $this->database);

        if ($this->db->connect_error) {
            die("Connection failed: " . $this->db->connect_error);
        }
    }

    public function getConnection() {
        return $this->db;
    }
}
?>
