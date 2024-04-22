create_table_Country = """
    CREATE TABLE IF NOT EXISTS "NDS".Country (
        CountryID SERIAL PRIMARY KEY,
        CountryName varchar(255)
    )
"""

create_table_Region = """
    CREATE TABLE IF NOT EXISTS "NDS".Region (
        RegionID SERIAL PRIMARY KEY,
        CountryID integer REFERENCES Country(CountryID),
        RegionName varchar(255)
    )
"""

create_table_Address = """
    CREATE TABLE IF NOT EXISTS "NDS".Address (
        AddressID SERIAL PRIMARY KEY,
        RegionID integer REFERENCES Region(RegionID),
        City varchar(255),
        AddressLine varchar(255)
    )
"""


create_table_Account = """
    CREATE TABLE IF NOT EXISTS "NDS".Account (
        AccountID SERIAL PRIMARY KEY,
        Username varchar(255),
        Password varchar(255),
        Role varchar(100)
    )
"""


create_table_UserInfo = """
    CREATE TABLE IF NOT EXISTS "NDS".UserInfo (
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
    CREATE TABLE IF NOT EXISTS "NDS".Field (
        FieldID SERIAL PRIMARY KEY,
        RegionID integer REFERENCES Region(RegionID),
        FieldName varchar(255),
        Area numeric(100,2)
    )
"""


create_table_RubberTree = """
    CREATE TABLE IF NOT EXISTS "NDS".RubberTree (
        TreeID SERIAL PRIMARY KEY,
        FieldID integer REFERENCES Field(FieldID),
        Location Point
    )
"""


create_table_RubberTreeInformation = """
    CREATE TABLE IF NOT EXISTS "NDS".RubberTreeInformation (
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
    CREATE TABLE IF NOT EXISTS "NDS".Plan (
        PlanID SERIAL PRIMARY KEY,
        Name varchar(255),
        Description varchar(255),
        StartDate timestamp
    )
"""

create_table_PlanDetail = """
    CREATE TABLE IF NOT EXISTS "NDS".PlanDetail (
        FieldID integer REFERENCES Field(fieldID),
        PlanID integer REFERENCES Plan(planID)
    )
"""

create_table_Lidar = """
    CREATE TABLE IF NOT EXISTS "NDS".Lidar (
        LidarID SERIAL PRIMARY KEY,
        Model varchar(255)
    )
"""

create_table_Camera = """
    CREATE TABLE IF NOT EXISTS "NDS".Camera (
        CameraID SERIAL PRIMARY KEY,
        Model varchar(255)
    )
"""

create_table_Radar = """
    CREATE TABLE IF NOT EXISTS "NDS".Radar (
        RadarID SERIAL PRIMARY KEY,
        Model varchar(255)
    )
"""

create_table_SensorControlSystem = """
    CREATE TABLE IF NOT EXISTS "NDS".SensorControlSystem (
        ScsID SERIAL PRIMARY KEY,
        LidarID integer REFERENCES Lidar(LidarID),
        CameraID integer REFERENCES Camera(CameraID),
        RadarID integer REFERENCES Radar(RadarID)
    )
"""


create_table_Robot = """
    CREATE TABLE IF NOT EXISTS "NDS".Robot (
        RobotID SERIAL PRIMARY KEY,
        TypeRobot varchar(255),
        Model varchar(255),
        Status Bool
    )
"""


create_table_Energy = """
    CREATE TABLE IF NOT EXISTS "NDS".Energy (
        EnergyID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        RemainingTime interval,
        RemainingEnergy numeric(100,2)
    )
"""

create_table_RobotTapping = """
    CREATE TABLE IF NOT EXISTS "NDS".RobotTapping (
        RobotTappingID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        TreeID integer references RubberTree(TreeID),
        Direction varchar(255),
        Speed numeric(100,2),
        Quantity numeric(100,2)
    )
"""

create_table_Blade = """
    CREATE TABLE IF NOT EXISTS "NDS".Blade (
        BladeID SERIAL PRIMARY KEY,
        RobotTappingID integer REFERENCES RobotTapping(RobotTappingID),
        TappingStatus varchar(255),
        Angle numeric(100,2),
        Depth numeric(100,2),
        BladeStatus varchar(255)
    )
"""


create_table_Environment = """
    CREATE TABLE IF NOT EXISTS "NDS".Environment (
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
    CREATE TABLE IF NOT EXISTS "NDS".Drone (
        DroneID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        ScsID integer REFERENCES SensorControlSystem(ScsID)
    )
"""

create_table_DroneInformation = """
    CREATE TABLE IF NOT EXISTS "NDS".DroneInformation (
        DroneInfoID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES Drone(DroneID),
        Direction varchar(255),
        Speed numeric(100,2),
        Height numeric(100,2),
        CurrentLocation point
    )
"""

create_table_DroneImage = """
    CREATE TABLE IF NOT EXISTS "NDS".DroneImage (
        DroneImageID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES Drone(DroneID),
        TreeID integer REFERENCES RubberTree(TreeID),
        Image Bytea
    )
"""


create_table_ChargingStation = """
    CREATE TABLE IF NOT EXISTS "NDS".ChargingStation (
        ChargingStationID SERIAL PRIMARY KEY,
        Location point,
        MaxRobotNumber integer,
        CurrentRobotNumber integer,
        Status varchar(255)
    )
"""


create_table_ChargingStatus = """
    CREATE TABLE IF NOT EXISTS "NDS".ChargingStatus (
        ChargingStatusID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES Robot(RobotID),
        ChargingStationID integer REFERENCES ChargingStation(ChargingStationID),
            CurrentBattery Numeric(100,2),
        Status bool
    )
"""


create_table_Task = """
    CREATE TABLE IF NOT EXISTS "NDS".Task (
        TaskID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES Robot(RobotID),
        PlanID integer REFERENCES Plan(PlanID),
        ActionDetail varchar(255)
    )
"""



