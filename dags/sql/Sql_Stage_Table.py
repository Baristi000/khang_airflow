create_table_Stage_Country = """
    CREATE TABLE "Stage".Country (
    CountryID SERIAL,
    CountryName varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Region = """
    CREATE TABLE "Stage".Region (
    RegionID SERIAL,
    CountryID integer,
    RegionName varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Address = """
    CREATE TABLE "Stage".Address (
    AddressID SERIAL,
    RegionID integer,
    City varchar(255),
    AddressLine varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Account = """
    CREATE TABLE "Stage".Account (
    AccountID SERIAL,
    Username varchar(255),
    Password varchar(255),
    Role varchar(100),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_UserInfo = """
    CREATE TABLE "Stage".UserInfo (
    UserID SERIAL,
    FirstName varchar(255),
    LastName varchar(255),
    Gender varchar(255),
    DateOfBirth date,
    AddressID integer,
    AccountID integer,
    Email varchar(255),
    PhoneNumber varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Field = """
    CREATE TABLE "Stage".Field (
    FieldID SERIAL,
    RegionID integer,
    FieldName varchar(255),
    Area numeric(100,2),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_RubberTree = """
    CREATE TABLE "Stage".RubberTree (
    TreeID SERIAL,
    FieldID integer,
    Location Point,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_RubberTreeInformation = """
    CREATE TABLE "Stage".RubberTreeInformation (
    TreeInfoID SERIAL,
    TreeID integer,
    TopHeight numeric(100,2),
    CrownHeight numeric(100,2),
    Diameter numeric(100,2),
    Circumference numeric(100,2),
    CheckDate timestamp,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Plan = """
    CREATE TABLE "Stage".Plan (
    PlanID SERIAL,
    Name varchar(255),
    Description varchar(255),
    StartDate timestamp,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_PlanDetail = """
    CREATE TABLE "Stage".PlanDetail (
    FieldID integer,
    PlanID integer,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Lidar = """
    CREATE TABLE "Stage".Lidar (
    LidarID SERIAL,
    Model varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Camera = """
    CREATE TABLE "Stage".Camera (
    CameraID SERIAL,
    Model varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Radar = """
    CREATE TABLE "Stage".Radar (
    RadarID SERIAL,
    Model varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_SensorControlSystem = """
    CREATE TABLE "Stage".SensorControlSystem (
    ScsID SERIAL,
    LidarID integer,
    CameraID integer,
    RadarID integer,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Robot = """
    CREATE TABLE "Stage".Robot (
    RobotID SERIAL,
    TypeRobot varchar(255),
    Model varchar(255),
    Status Bool,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Energy = """
    CREATE TABLE "Stage".Energy (
    EnergyID SERIAL,
    RobotID integer,
    RemainingTime interval,
    RemainingEnergy numeric(100,2),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_RobotTapping = """
    CREATE TABLE "Stage".RobotTapping (
    RobotTappingID SERIAL,
    RobotID integer,
    TreeID integer,
    Direction varchar(255),
    Speed numeric(100,2),
    Quantity numeric(100,2),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Blade = """
    CREATE TABLE "Stage".Blade (
    BladeID SERIAL,
    RobotTappingID integer,
    TappingStatus varchar(255),
    Angle numeric(100,2),
    Depth numeric(100,2),
    BladeStatus varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Environment = """
    CREATE TABLE "Stage".Environment (
    EnvironmentID SERIAL,
    RobotTappingID integer,
    WindDirection varchar(255),
    WindSpeed numeric(100,2),
    Temperature numeric(100,2),
    Rainfall numeric(100,2),
    Time timestamp,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Drone = """
    CREATE TABLE "Stage".Drone (
    DroneID SERIAL,
    RobotID integer,
    ScsID integer,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_DroneInformation = """
    CREATE TABLE "Stage".DroneInformation (
    DroneInfoID SERIAL,
    DroneID integer,
    Direction varchar(255),
    Speed numeric(100,2),
    Height numeric(100,2),
    CurrentLocation point,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_DroneImage = """
CREATE TABLE "Stage".DroneImage (
DroneImageID SERIAL,
DroneID integer,
TreeID integer,
Image Bytea,
CreatedDate Timestamp DEFAULT NOW(),
UpdateDate timestamp DEFAULT NOW()
);
"""

create_table_Stage_ChargingStation = """
    CREATE TABLE "Stage".ChargingStation (
    ChargingStationID SERIAL,
    Location point,
    MaxRobotNumber integer,
    CurrentRobotNumber integer,
    Status varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_ChargingStatus = """
    CREATE TABLE "Stage".ChargingStatus (
    ChargingStatusID SERIAL,
    DroneID integer,
    ChargingStationID integer,
    CurrentBattery Numeric(100,2),
    Status bool,
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_Stage_Task = """
    CREATE TABLE "Stage".Task (
    TaskID SERIAL,
    RobotID integer,
    PlanID integer,
    ActionDetail varchar(255),
    CreatedDate Timestamp DEFAULT NOW(),
    UpdateDate timestamp DEFAULT NOW()
    );
"""