<?php
$servername = "localhost";
$username = "root";
$password = "NO";
$dbname = "Airborne";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the data from the POST request
//$data = json_decode(file_get_contents('try_flask_postdata.html'), true);

//$passportID = isset($_POST['passportID']) ? $_POST['passportID'] :null;
$name = isset($_POST['name']) ? $_POST['name'] : null;
$age = isset($_POST['age']) ? $_POST['age'] : null;
$email = isset($_POST['email']) ? $_POST['email'] : null;

// Prepare and bind
$stmt = $conn->prepare("INSERT INTO Passenger (name, age, email) VALUES (?, ?, ?)");
$stmt->bind_param("sis", $name, $age, $email);

// Execute the statement
$stmt->execute();

echo "New record created successfully";

$stmt->close();
$conn->close();
?>