-- Vložení záznamù do tabulky Users
INSERT INTO Users (First_name, Last_name, Email, Password, Status, Verified)
VALUES 
  ('John', 'Doe', 'john.doe@example.com', 'password123', 'Active', 1),
  ('Jane', 'Smith', 'jane.smith@example.com', 'securepass', 'Inactive', 0),
  ('Alice', 'Johnson', 'alice.johnson@example.com', 'pass123', 'Blocked', 1),
  ('Bob', 'Williams', 'bob.williams@example.com', 'bobs_pass', 'Active', 0),
  ('Eva', 'Miller', 'eva.miller@example.com', 'evapassword', 'Inactive', 1);

-- Vložení záznamù do tabulky Roles
INSERT INTO Roles (Role_name, Role_description)
VALUES 
  ('Admin', 'Administrator with full access'),
  ('User', 'Regular user with limited access'),
  ('Manager', 'Manager with intermediate access'),
  ('Guest', 'Limited access as a guest'),
  ('Support', 'Support role with specific permissions');

-- Vložení záznamù do tabulky Permissions
INSERT INTO Permissions (Permission_name, Permission_description)
VALUES 
  ('Read', 'Read-only permission'),
  ('Write', 'Write permission'),
  ('Execute', 'Execute permission'),
  ('Administrate', 'Full administrative permission'),
  ('Report', 'Permission to generate reports');

-- Vložení záznamù do tabulky UserRoles
INSERT INTO UserRoles (Users_ID, Roles_ID, Date_of_assignment)
VALUES 
  (1, 1, GETDATE()),
  (2, 2, GETDATE()),
  (3, 3, GETDATE()),
  (4, 1, GETDATE()),
  (5, 2, GETDATE());

-- Vložení záznamù do tabulky RolePermissions
INSERT INTO RolePermissions (Roles_ID, Permissions_ID)
VALUES 
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5);

-- Vložení záznamù do tabulky Logs
INSERT INTO Logs (Users_ID, Action, Action_time, Status)
VALUES 
  (1, 'Login', GETDATE(), 'Success'),
  (2, 'Update Profile', GETDATE(), 'Failure'),
  (3, 'Logout', GETDATE(), 'Warning'),
  (4, 'Create New Document', GETDATE(), 'Success'),
  (5, 'Delete Account', GETDATE(), 'Failure');