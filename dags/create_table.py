create_table_Country = """
    CREATE TABLE Country (
        CountryID SERIAL PRIMARY KEY,
        CountryName varchar(255)
    )
"""

create_table_Region = """
    CREATE TABLE Region (
        RegionID SERIAL PRIMARY KEY,
        CountryID integer REFERENCES Country(CountryID),
        RegionName varchar(255)
    )
"""

create_table_Address = """
    CREATE TABLE Address (
        AddressID SERIAL PRIMARY KEY,
        RegionID integer REFERENCES Region(RegionID),
        City varchar(255),
        AddressLine varchar(255)
    )
"""


create_table_Account = """"
    CREATE TABLE Account (
        AccountID SERIAL PRIMARY KEY,
        Username varchar(255),
        Password varchar(255),
        Role varchar(100)
    )
"""


create_table_UserInfo = """
    CREATE TABLE UserInfo (
        UserID SERIAL PRIMARY KEY,
        FirstName varchar(255),
        LastName varchar(255),
        Gender varchar(255),
        DateOfBirth date,
        AddressID integer REFERENCES Address(AddressID),
        AccountID integer REFERENCES Account(AccountID),
        Email varchar(255),
        PhoneNumber varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp
    )
"""


create_table_Field = """
    CREATE TABLE Field (
        FieldID SERIAL PRIMARY KEY,
        RegionID integer REFERENCES Region(RegionID),
        FieldName varchar(255),
        Area numeric(100,2)
    )
"""


create_table_RubberTree = """
    CREATE TABLE RubberTree (
        TreeID SERIAL PRIMARY KEY,
        FieldID integer REFERENCES Field(FieldID),
        Location Point
    )
"""


create_table_RubberTreeInformation = """
    CREATE TABLE RubberTreeInformation (
        TreeInfoID SERIAL PRIMARY KEY,
        TreeID integer REFERENCES RubberTree(TreeID),
        TopHeight numeric(100,2),
        CrownHeight numeric(100,2),
        Diameter numeric(100,2),
        Circumference numeric(100,2),
        CheckDate timestamp
    )
"""

create_table_Plan = """
    CREATE TABLE Plan (
        PlanID SERIAL PRIMARY KEY,
        Name varchar(255),
        Description varchar(255),
        StartDate timestamp
    )
"""

create_table_PlanDetail = """
    CREATE TABLE PlanDetail (
        FieldID integer REFERENCES Field(fieldID),
        PlanID integer REFERENCES Plan(planID)
    )
"""

create_table_Lidar = """
    CREATE TABLE Lidar (
        LidarID SERIAL PRIMARY KEY,
        Model varchar(255)
    )
"""

create_table_Camera = """
    CREATE TABLE Camera (
        CameraID SERIAL PRIMARY KEY,
        Model varchar(255)
    )
"""

create_table_Radar = """
    CREATE TABLE Radar (
        RadarID SERIAL PRIMARY KEY,
        Model varchar(255)
    )
"""

create_table_SensorControlSystem = """
    CREATE TABLE SensorControlSystem (
        ScsID SERIAL PRIMARY KEY,
        LidarID integer REFERENCES Lidar(LidarID),
        CameraID integer REFERENCES Camera(CameraID),
        RadarID integer REFERENCES Radar(RadarID)
    )
"""


create_table_Robot = """
    CREATE TABLE Robot (
        RobotID SERIAL PRIMARY KEY,
        TypeRobot varchar(255),
        Model varchar(255),
        Status Bool
    )
"""


create_table_Energy = """
    CREATE TABLE Energy (
        EnergyID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        RemainingTime interval,
        RemainingEnergy numeric(100,2)
    )
"""

create_table_RobotTapping = """
    CREATE TABLE RobotTapping (
        RobotTappingID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        TreeID integer references RubberTree(TreeID),
        Direction varchar(255),
        Speed numeric(100,2),
        Quantity numeric(100,2)
    )
"""

create_table_Blade = """
    CREATE TABLE Blade (
        BladeID SERIAL PRIMARY KEY,
        RobotTappingID integer REFERENCES RobotTapping(RobotTappingID),
        TappingStatus varchar(255),
        Angle numeric(100,2),
        Depth numeric(100,2),
        BladeStatus varchar(255)
    )
"""


create_table_Environment = """
    CREATE TABLE Environment (
        EnvironmentID SERIAL PRIMARY KEY,
        RobotTappingID integer REFERENCES RobotTapping(RobotTappingID),
        WindDirection varchar(255),
        WindSpeed numeric(100,2),
        Temperature numeric(100,2),
        Rainfall numeric(100,2),
        Time timestamp
    )

"""

create_table_Drone = """
    CREATE TABLE Drone (
        DroneID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        ScsID integer REFERENCES SensorControlSystem(ScsID)
    )
"""

create_table_DroneInformation = """
    CREATE TABLE DroneInformation (
        DroneInfoID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES Drone(DroneID),
        Direction varchar(255),
        Speed numeric(100,2),
        Height numeric(100,2),
        CurrentLocation point
    )
"""

create_table_DroneImage = """
    CREATE TABLE DroneImage (
        DroneImageID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES Drone(DroneID),
        TreeID integer REFERENCES RubberTree(TreeID),
        Image Bytea
    )
"""


create_table_ChargingStation = """
    CREATE TABLE ChargingStation (
        ChargingStationID SERIAL PRIMARY KEY,
        Location point,
        MaxRobotNumber integer,
        CurrentRobotNumber integer,
        Status varchar(255)
    )
"""


create_table_ChargingStatus = """
    CREATE TABLE ChargingStatus (
        ChargingStatusID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES Robot(RobotID),
        ChargingStationID integer REFERENCES ChargingStation(ChargingStationID),
            CurrentBattery Numeric(100,2),
        Status bool
    )
"""


create_table_Task = """
    CREATE TABLE Task (
        TaskID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        PlanID integer REFERENCES Plan(PlanID),
        ActionDetail varchar(255)
    )
"""



