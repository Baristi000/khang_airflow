create_table_Source_Country = """
    CREATE TABLE "Source".Country (
    CountryID SERIAL ,
    CountryName varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Region = """
    CREATE TABLE "Source".Region (
    RegionID SERIAL ,
    CountryID integer ,
    RegionName varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Address = """
    CREATE TABLE "Source".Address (
    AddressID SERIAL ,
    RegionID integer ,
    City varchar(255),
    AddressLine varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Account = """
    CREATE TABLE "Source".Account (
    AccountID SERIAL ,
    Username varchar(255),
    Password varchar(255),
    Role varchar(100),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_UserInfo = """
    CREATE TABLE "Source".UserInfo (
    UserID SERIAL ,
    FirstName varchar(255),
    LastName varchar(255),
    Gender varchar(255),
    DateOfBirth date,
    AddressID integer ,
    AccountID integer ,
    Email varchar(255),
    PhoneNumber varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Field = """
    CREATE TABLE "Source".Field (
    FieldID SERIAL ,
    RegionID integer ,
    FieldName varchar(255),
    Area numeric(100,2),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_RubberTree = """
    CREATE TABLE "Source".RubberTree (
    TreeID SERIAL ,
    FieldID integer ,
    Location Point,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_RubberTreeInformation = """
    CREATE TABLE "Source".RubberTreeInformation (
    TreeInfoID SERIAL ,
    TreeID integer ,
    TopHeight numeric(100,2),
    CrownHeight numeric(100,2),
    Diameter numeric(100,2),
    Circumference numeric(100,2),
    CheckDate timestamp,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Plan = """
    CREATE TABLE "Source".Plan (
    PlanID SERIAL ,
    Name varchar(255),
    Description varchar(255),
    StartDate timestamp,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_PlanDetail = """
    CREATE TABLE "Source".PlanDetail (
    FieldID integer ,
    PlanID integer ,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Lidar = """
    CREATE TABLE "Source".Lidar (
    LidarID SERIAL ,
    Model varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Camera = """
    CREATE TABLE "Source".Camera (
    CameraID SERIAL ,
    Model varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Radar = """
    CREATE TABLE "Source".Radar (
    RadarID SERIAL ,
    Model varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_SensorControlSystem = """
    CREATE TABLE "Source".SensorControlSystem (
    ScsID SERIAL ,
    LidarID integer ,
    CameraID integer ,
    RadarID integer ,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Robot = """
    CREATE TABLE "Source".Robot (
    RobotID SERIAL ,
    TypeRobot varchar(255),
    Model varchar(255),
    Status Bool,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Energy = """
    CREATE TABLE "Source".Energy (
    EnergyID SERIAL ,
    RobotID integer ,
    RemainingTime interval,
    RemainingEnergy numeric(100,2),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_RobotTapping = """
    CREATE TABLE "Source".RobotTapping (
    RobotTappingID SERIAL ,
    RobotID integer ,
    TreeID integer ,
    Direction varchar(255),
    Speed numeric(100,2),
    Quantity numeric(100,2),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Blade = """
    CREATE TABLE "Source".Blade (
    BladeID SERIAL ,
    RobotTappingID integer ,
    TappingStatus varchar(255),
    Angle numeric(100,2),
    Depth numeric(100,2),
    BladeStatus varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Environment = """
    CREATE TABLE "Source".Environment (
    EnvironmentID SERIAL ,
    RobotTappingID integer ,
    WindDirection varchar(255),
    WindSpeed numeric(100,2),
    Temperature numeric(100,2),
    Rainfall numeric(100,2),
    Time timestamp,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Drone = """
    CREATE TABLE "Source".Drone (
    DroneID SERIAL ,
    RobotID integer ,
    ScsID integer ,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_DroneInformation = """
    CREATE TABLE "Source".DroneInformation (
    DroneInfoID SERIAL ,
    DroneID integer ,
    Direction varchar(255),
    Speed numeric(100,2),
    Height numeric(100,2),
    CurrentLocation point,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_DroneImage = """
    CREATE TABLE "Source".DroneImage (
    DroneImageID SERIAL ,
    DroneID integer ,
    TreeID integer ,
    Image Bytea,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_ChargingStation = """
    CREATE TABLE "Source".ChargingStation (
    ChargingStationID SERIAL ,
    Location point,
    MaxRobotNumber integer,
    CurrentRobotNumber integer,
    Status varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_ChargingStatus = """
    CREATE TABLE "Source".ChargingStatus (
    ChargingStatusID SERIAL ,
    DroneID integer ,
    ChargingStationID integer ,
    CurrentBattery Numeric(100,2),
    Status bool,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Source_Task = """
    CREATE TABLE "Source".Task (
    TaskID SERIAL ,
    RobotID integer ,
    PlanID integer ,
    ActionDetail varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""