use AirPort;

CREATE TABLE if not EXISTS Airport (
    IATA VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) not null
);

CREATE TABLE IF NOT EXISTS Hanger (
    Hanger_number INT PRIMARY KEY,
    capacity INT not null,
    location VARCHAR(255) not null,
    isAvailable BOOLEAN not null,
    airport VARCHAR(255),
    airplane INT,
    --FOREIGN KEY (airport) REFERENCES Airport(IATA),
    --FOREIGN KEY (airplane) REFERENCES AirPlane(registration_number)
);

CREATE TABLE IF NOT EXISTS Gate (
    Gate_number INT PRIMARY KEY,
    location VARCHAR(255) not null,
    isAvailable BOOLEAN not null,
    airport VARCHAR(255),
    --FOREIGN KEY (airport) REFERENCES Airport(IATA)
);

CREATE TABLE IF NOT EXISTS Employee (
    employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) not null,
    Age INT not null,
    Department VARCHAR(255) not null,
    Job_Title VARCHAR(255) not null,
    Salary INT,
    Phone_number VARCHAR(255) not null,
    Email VARCHAR(255),
    Hire_date DATE not null
);

CREATE TABLE IF not EXISTS Airlines (
    Name VARCHAR(255) PRIMARY KEY,
    Country VARCHAR(255),
    establishedYear INT not null,
    Owner VARCHAR(255) not null,
    isInternational BOOLEAN,
    flights INT,
    --FOREIGN KEY (flights) REFERENCES Flight(flight_number)
);

CREATE TABLE IF NOT EXISTS AirPlane (
    Registration_number INT PRIMARY KEY,
    Manufacturer VARCHAR(255) not null,
    Model VARCHAR(255) not null,
    max_capacity INT not null,
    Max_range INT not null,
    yearofManufacture INT not null,
    Fuel_type VARCHAR(255) not null,
    Currunt_status VARCHAR(255) not null,
    Operator VARCHAR(255),
    Owner VARCHAR(255),
);


CREATE TABLE IF NOT EXISTS Flight (
    flight_number INT PRIMARY KEY,
    DATE DATE not null,
    departureTime DATETIME not null,
    arrivalTime DATETIME not null,
    Departure_AirPort VARCHAR(255) not null,
    Arrival_AirPort VARCHAR(255) not null,
    airplane VARCHAR(255) not null,
    --FOREIGN KEY (airplane) REFERENCES AirPlane(Registration_number),
    --FOREIGN KEY (Departure_Ai 0rPort) REFERENCES Airport(IATA),
    --FOREIGN KEY (Arrival_AirPort) REFERENCES Airport(IATA)
);

CREATE TABLE IF NOT EXISTS Passenger (
    passportID INT PRIMARY KEY,
    nationality VARCHAR(255) not null,
    name VARCHAR(255) not null,
    age INT not null,
    gender VARCHAR(255) not null,
    phone_number VARCHAR(255) not null,
    email VARCHAR(255),
    address VARCHAR(255),
    flight INT,
    --FOREIGN KEY (flight) REFERENCES Flight(flight_number)
);

CREATE TABLE IF NOT EXISTS Ticket (
    ticket_number INT PRIMARY KEY,
    price INT not null,
    seat VARCHAR(255) not null,
    class VARCHAR(255) not null,
    passenger INT,
    flight INT,
    --FOREIGN KEY (passenger) REFERENCES Passenger(passportID),
    --FOREIGN KEY (flight) REFERENCES Flight(flight_number)
);

CREATE table if not EXISTS Airline_Employee (
    employee_ID INT PRIMARY KEY,
    airline VARCHAR(255),
    --FOREIGN KEY (employee_ID) REFERENCES Employee(employee_ID),
    --FOREIGN KEY (airline) REFERENCES Airlines(Name)
);
