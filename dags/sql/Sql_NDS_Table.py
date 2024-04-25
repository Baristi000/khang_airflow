create_table_NDS_Country = """
    CREATE TABLE "NDS".Country (
        CountryID SERIAL PRIMARY KEY,
        CountryName varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Region = """
    CREATE TABLE "NDS".Region (
        RegionID SERIAL PRIMARY KEY,
        CountryID integer REFERENCES "NDS".Country(CountryID),
        RegionName varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Address = """
    CREATE TABLE "NDS".Address (
        AddressID SERIAL PRIMARY KEY,
        RegionID integer REFERENCES "NDS".Region(RegionID),
        City varchar(255),
        AddressLine varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Account = """
    CREATE TABLE "NDS".Account (
        AccountID SERIAL PRIMARY KEY,
        Username varchar(255),
        Password varchar(255),
        Role varchar(100),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_UserInfo = """
    CREATE TABLE "NDS".UserInfo (
        UserID SERIAL PRIMARY KEY,
        FirstName varchar(255),
        LastName varchar(255),
        Gender varchar(255),
        DateOfBirth date,
        AddressID integer REFERENCES "NDS".Address(AddressID),
        AccountID integer REFERENCES "NDS".Account(AccountID),
        Email varchar(255),
        PhoneNumber varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp
    );
"""

create_table_NDS_Field = """
    CREATE TABLE "NDS".Field (
        FieldID SERIAL PRIMARY KEY,
        RegionID integer REFERENCES "NDS".Region(RegionID),
        FieldName varchar(255),
        Area numeric(100,2),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_RubberTree = """
    CREATE TABLE "NDS".RubberTree (
        TreeID SERIAL PRIMARY KEY,
        FieldID integer REFERENCES "NDS".Field(FieldID),
        Location Point,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_RubberTreeInformation = """
    CREATE TABLE "NDS".RubberTreeInformation (
        TreeInfoID SERIAL PRIMARY KEY,
        TreeID integer REFERENCES "NDS".RubberTree(TreeID),
        TopHeight numeric(100,2),
        CrownHeight numeric(100,2),
        Diameter numeric(100,2),
        Circumference numeric(100,2),
        CheckDate timestamp,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Plan = """
    CREATE TABLE "NDS".Plan (
        PlanID SERIAL PRIMARY KEY,
        Name varchar(255),
        Description varchar(255),
        StartDate timestamp,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_PlanDetail = """
    CREATE TABLE "NDS".PlanDetail (
        FieldID integer REFERENCES "NDS".Field(fieldID),
        PlanID integer REFERENCES "NDS".Plan(planID),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW(),
        CONSTRAINT pk_PlanDetail PRIMARY KEY (FieldID, PlanID)
    );
"""

create_table_NDS_Lidar = """
    CREATE TABLE "NDS".Lidar (
        LidarID SERIAL PRIMARY KEY,
        Model varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Camera = """
    CREATE TABLE "NDS".Camera (
        CameraID SERIAL PRIMARY KEY,
        Model varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Radar = """
    CREATE TABLE "NDS".Radar (
        RadarID SERIAL PRIMARY KEY,
        Model varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_SensorControlSystem = """
    CREATE TABLE "NDS".SensorControlSystem (
        ScsID SERIAL PRIMARY KEY,
        LidarID integer REFERENCES "NDS".Lidar(LidarID),
        CameraID integer REFERENCES "NDS".Camera(CameraID),
        RadarID integer REFERENCES "NDS".Radar(RadarID),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Robot = """
    CREATE TABLE "NDS".Robot (
        RobotID SERIAL PRIMARY KEY,
        TypeRobot varchar(255),
        Model varchar(255),
        Status Bool,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Energy = """
    CREATE TABLE "NDS".Energy (
        EnergyID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES "NDS".Robot(RobotID),
        RemainingTime interval,
        RemainingEnergy numeric(100,2),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_RobotTapping = """
    CREATE TABLE "NDS".RobotTapping (
        RobotTappingID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES "NDS".Robot(RobotID),
        TreeID integer REFERENCES "NDS".RubberTree(TreeID),
        Direction varchar(255),
        Speed numeric(100,2),
        Quantity numeric(100,2),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Blade = """
    CREATE TABLE "NDS".Blade (
        BladeID SERIAL PRIMARY KEY,
        RobotTappingID integer REFERENCES "NDS".RobotTapping(RobotTappingID),
        TappingStatus varchar(255),
        Angle numeric(100,2),
        Depth numeric(100,2),
        BladeStatus varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Environment = """
    CREATE TABLE "NDS".Environment (
        EnvironmentID SERIAL PRIMARY KEY,
        RobotTappingID integer REFERENCES "NDS".RobotTapping(RobotTappingID),
        WindDirection varchar(255),
        WindSpeed numeric(100,2),
        Temperature numeric(100,2),
        Rainfall numeric(100,2),
        Time timestamp,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Drone = """
    CREATE TABLE "NDS".Drone (
        DroneID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES "NDS".Robot(RobotID),
        ScsID integer REFERENCES "NDS".SensorControlSystem(ScsID),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_DroneInformation = """
    CREATE TABLE "NDS".DroneInformation (
        DroneInfoID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES "NDS".Drone(DroneID),
        Direction varchar(255),
        Speed numeric(100,2),
        Height numeric(100,2),
        CurrentLocation point,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_DroneImage = """
    CREATE TABLE "NDS".DroneImage (
        DroneImageID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES "NDS".Drone(DroneID),
        TreeID integer REFERENCES "NDS".RubberTree(TreeID),
        Image Bytea,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_ChargingStation = """
    CREATE TABLE "NDS".ChargingStation (
        ChargingStationID SERIAL PRIMARY KEY,
        Location point,
        MaxRobotNumber integer,
        CurrentRobotNumber integer,
        Status varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_ChargingStatus = """
    CREATE TABLE "NDS".ChargingStatus (
        ChargingStatusID SERIAL PRIMARY KEY,
        DroneID integer REFERENCES "NDS".Drone(DroneID),
        ChargingStationID integer REFERENCES "NDS".ChargingStation(ChargingStationID),
        CurrentBattery Numeric(100,2),
        Status bool,
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""

create_table_NDS_Task = """
    CREATE TABLE "NDS".Task (
        TaskID SERIAL PRIMARY KEY,
        RobotID integer REFERENCES "NDS".Robot(RobotID),
        PlanID integer REFERENCES "NDS".Plan(PlanID),
        ActionDetail varchar(255),
        CreatedDate Timestamp DEFAULT NOW(),
        UpdateDate timestamp DEFAULT NOW()
    );
"""