<?php

$server_name="localhost";
$user_name="root";
$password="kaushiknk";

// Create connection
$conn = new mysqli($server_name, $user_name, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
?>