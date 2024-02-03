-- Vytvoøení tabulky Uživatelé (Users)
CREATE TABLE Users (
  ID INT PRIMARY KEY identity(1,1),
  First_name varchar(30) NOT NULL,
  Last_name varchar(30) NOT NULL,
  Email varchar(30) NOT NULL UNIQUE CHECK (Email LIKE '%_@_%._%'),
  Password varchar(30) NOT NULL,
  Registration_date DATETIME DEFAULT GETDATE(),
  Status varchar(20) NOT NULL CHECK (Status IN ('Active','Inactive','Blocked')) DEFAULT 'Active',
  Verified BIT DEFAULT 0 -- Logická hodnota pro ovìøení uživatele (0 = neovìøený, 1 = ovìøený)
);

-- Vytvoøení tabulky Role (Roles)
CREATE TABLE Roles (
  ID INT PRIMARY KEY identity(1,1),
  Role_name varchar(50) NOT NULL UNIQUE,
  Role_description varchar(200)
);

-- Vytvoøení tabulky Práva (Permissions)
CREATE TABLE Permissions (
  ID INT PRIMARY KEY identity(1,1),
  Permission_name varchar(50) NOT NULL UNIQUE,
  Permission_description varchar(200)
);

-- Vytvoøení tabulky Uživatelské Role (UserRoles)
CREATE TABLE UserRoles (
  ID INT PRIMARY KEY identity(1,1),
  Users_ID INT FOREIGN KEY REFERENCES Users(ID),
  Roles_ID INT FOREIGN KEY REFERENCES Roles(ID),
  Date_of_assignment DATETIME DEFAULT GETDATE()
);

-- Vytvoøení tabulky Role Práva (RolePermissions)
CREATE TABLE RolePermissions (
  ID INT PRIMARY KEY identity(1,1),
  Roles_ID INT FOREIGN KEY REFERENCES Roles(ID),
  Permissions_ID INT FOREIGN KEY REFERENCES Permissions(ID)
);

-- Vytvoøení tabulky Log (Logs)
CREATE TABLE Logs (
  ID INT PRIMARY KEY identity(1,1),
  Users_ID INT FOREIGN KEY REFERENCES Users(ID),
  Action varchar(50) NOT NULL,
  Action_time DATETIME DEFAULT GETDATE(),
  Status varchar(20) NOT NULL CHECK (Status IN ('Success', 'Failure', 'Warning'))
);