-- Vytvo�en� tabulky U�ivatel� (Users)
CREATE TABLE Users (
  ID INT PRIMARY KEY identity(1,1),
  First_name varchar(30) NOT NULL,
  Last_name varchar(30) NOT NULL,
  Email varchar(30) NOT NULL UNIQUE CHECK (Email LIKE '%_@_%._%'),
  Password varchar(30) NOT NULL,
  Registration_date DATETIME DEFAULT GETDATE(),
  Status varchar(20) NOT NULL CHECK (Status IN ('Active','Inactive','Blocked')) DEFAULT 'Active',
  Verified BIT DEFAULT 0 -- Logick� hodnota pro ov��en� u�ivatele (0 = neov��en�, 1 = ov��en�)
);

-- Vytvo�en� tabulky Role (Roles)
CREATE TABLE Roles (
  ID INT PRIMARY KEY identity(1,1),
  Role_name varchar(50) NOT NULL UNIQUE,
  Role_description varchar(200)
);

-- Vytvo�en� tabulky Pr�va (Permissions)
CREATE TABLE Permissions (
  ID INT PRIMARY KEY identity(1,1),
  Permission_name varchar(50) NOT NULL UNIQUE,
  Permission_description varchar(200)
);

-- Vytvo�en� tabulky U�ivatelsk� Role (UserRoles)
CREATE TABLE UserRoles (
  ID INT PRIMARY KEY identity(1,1),
  Users_ID INT FOREIGN KEY REFERENCES Users(ID),
  Roles_ID INT FOREIGN KEY REFERENCES Roles(ID),
  Date_of_assignment DATETIME DEFAULT GETDATE()
);

-- Vytvo�en� tabulky Role Pr�va (RolePermissions)
CREATE TABLE RolePermissions (
  ID INT PRIMARY KEY identity(1,1),
  Roles_ID INT FOREIGN KEY REFERENCES Roles(ID),
  Permissions_ID INT FOREIGN KEY REFERENCES Permissions(ID)
);

-- Vytvo�en� tabulky Log (Logs)
CREATE TABLE Logs (
  ID INT PRIMARY KEY identity(1,1),
  Users_ID INT FOREIGN KEY REFERENCES Users(ID),
  Action varchar(50) NOT NULL,
  Action_time DATETIME DEFAULT GETDATE(),
  Status varchar(20) NOT NULL CHECK (Status IN ('Success', 'Failure', 'Warning'))
);