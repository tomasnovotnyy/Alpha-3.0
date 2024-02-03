-- Databázový pohled pro vypsání informací o uživatelích a jejich rolích
CREATE VIEW UserRolesView AS
SELECT
    U.ID AS User_ID,
    U.First_name,
    U.Last_name,
    U.Email,
    R.Role_name,
    L.Action,
    L.Status
FROM Users U
LEFT JOIN UserRoles UR ON U.ID = UR.Users_ID
LEFT JOIN Roles R ON UR.Roles_ID = R.ID
LEFT JOIN Logs L ON U.ID = L.Users_ID
GROUP BY
    U.ID,
    U.First_name,
    U.Last_name,
    U.Email,
    R.Role_name,
    L.Action,
	L.Status;

-- Databázový pohled pro záznamy logù spolu s informacemi o uživatelských akcích
CREATE VIEW UserLogsView AS
SELECT
    L.ID AS Log_ID,
    U.First_name,
    U.Last_name,
	U.Email,
    L.Action,
    L.Action_time,
    L.Status
FROM Logs L
JOIN Users U ON L.Users_ID = U.ID;