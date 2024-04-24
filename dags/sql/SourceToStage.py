truncateTableAndSetCet_Country = ''' 
    TRUNCATE table "Stage".Country;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Country' 
'''
sourceToStage_Country = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Country';

        INSERT INTO "Stage".Country 
        SELECT * FROM "Source".Country 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Country = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Country' 
'''
##------------------
truncateTableAndSetCet_Region = ''' 
    TRUNCATE table "Stage".Region;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Region' 
'''
sourceToStage_Region = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Region';

        INSERT INTO "Stage".Region 
        SELECT * FROM "Source".Region 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Region = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Region' 
'''
##------------------
truncateTableAndSetCet_Address = ''' 
    TRUNCATE table "Stage".Address;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Address' 
'''
sourceToStage_Address = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Address';

        INSERT INTO "Stage".Address 
        SELECT * FROM "Source".Address 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Address = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Address' 
'''
##------------------
truncateTableAndSetCet_Account = ''' 
    TRUNCATE table "Stage".Account;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Account' 
'''
sourceToStage_Account = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Account';

        INSERT INTO "Stage".Account 
        SELECT * FROM "Source".Account 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Account = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Account' 
'''
##------------------
truncateTableAndSetCet_UserInfo = ''' 
    TRUNCATE table "Stage".UserInfo;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'UserInfo' 
'''
sourceToStage_UserInfo = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'UserInfo';

        INSERT INTO "Stage".UserInfo 
        SELECT * FROM "Source".UserInfo 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_UserInfo = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'UserInfo' 
'''
##------------------
truncateTableAndSetCet_Field = ''' 
    TRUNCATE table "Stage".Field;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Field' 
'''
sourceToStage_Field = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Field';

        INSERT INTO "Stage".Field 
        SELECT * FROM "Source".Field 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Field = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Field' 
'''
##------------------
truncateTableAndSetCet_RubberTree = ''' 
    TRUNCATE table "Stage".RubberTree;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'RubberTree' 
'''
sourceToStage_RubberTree = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'RubberTree';

        INSERT INTO "Stage".RubberTree 
        SELECT * FROM "Source".RubberTree 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_RubberTree = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'RubberTree' 
'''
##------------------
truncateTableAndSetCet_RubberTreeInformation = ''' 
    TRUNCATE table "Stage".RubberTreeInformation;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'RubberTreeInformation' 
'''
sourceToStage_RubberTreeInformation = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'RubberTreeInformation';

        INSERT INTO "Stage".RubberTreeInformation 
        SELECT * FROM "Source".RubberTreeInformation 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_RubberTreeInformation = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'RubberTreeInformation' 
'''
##------------------
truncateTableAndSetCet_Plan = ''' 
    TRUNCATE table "Stage".Plan;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Plan' 
'''
sourceToStage_Plan = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Plan';

        INSERT INTO "Stage".Plan 
        SELECT * FROM "Source".Plan 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Plan = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Plan' 
'''
##------------------
truncateTableAndSetCet_PlanDetail = ''' 
    TRUNCATE table "Stage".PlanDetail;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'PlanDetail' 
'''
sourceToStage_PlanDetail = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'PlanDetail';

        INSERT INTO "Stage".PlanDetail 
        SELECT * FROM "Source".PlanDetail 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_PlanDetail = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'PlanDetail' 
'''
##------------------
truncateTableAndSetCet_Lidar = ''' 
    TRUNCATE table "Stage".Lidar;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Lidar' 
'''
sourceToStage_Lidar = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Lidar';

        INSERT INTO "Stage".Lidar 
        SELECT * FROM "Source".Lidar 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Lidar = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Lidar' 
'''
##------------------
truncateTableAndSetCet_Camera = ''' 
    TRUNCATE table "Stage".Camera;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Camera' 
'''
sourceToStage_Camera = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Camera';

        INSERT INTO "Stage".Camera 
        SELECT * FROM "Source".Camera 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Camera = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Camera' 
'''
##------------------
truncateTableAndSetCet_Radar = ''' 
    TRUNCATE table "Stage".Radar;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Radar' 
'''
sourceToStage_Radar = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Radar';

        INSERT INTO "Stage".Radar 
        SELECT * FROM "Source".Radar 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Radar = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Radar' 
'''
##------------------
truncateTableAndSetCet_SensorControlSystem = ''' 
    TRUNCATE table "Stage".SensorControlSystem;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'SensorControlSystem' 
'''
sourceToStage_SensorControlSystem = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'SensorControlSystem';

        INSERT INTO "Stage".SensorControlSystem 
        SELECT * FROM "Source".SensorControlSystem 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_SensorControlSystem = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'SensorControlSystem' 
'''
##------------------
truncateTableAndSetCet_Robot = ''' 
    TRUNCATE table "Stage".Robot;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Robot' 
'''
sourceToStage_Robot = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Robot';

        INSERT INTO "Stage".Robot 
        SELECT * FROM "Source".Robot 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Robot = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Robot' 
'''
##------------------
truncateTableAndSetCet_Energy = ''' 
    TRUNCATE table "Stage".Energy;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Energy' 
'''
sourceToStage_Energy = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Energy';

        INSERT INTO "Stage".Energy 
        SELECT * FROM "Source".Energy 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Energy = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Energy' 
'''
##------------------
truncateTableAndSetCet_RobotTapping = ''' 
    TRUNCATE table "Stage".RobotTapping;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'RobotTapping' 
'''
sourceToStage_RobotTapping = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'RobotTapping';

        INSERT INTO "Stage".RobotTapping 
        SELECT * FROM "Source".RobotTapping 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_RobotTapping = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'RobotTapping' 
'''
##------------------
truncateTableAndSetCet_Blade = ''' 
    TRUNCATE table "Stage".Blade;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Blade' 
'''
sourceToStage_Blade = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Blade';

        INSERT INTO "Stage".Blade 
        SELECT * FROM "Source".Blade 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Blade = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Blade' 
'''
##------------------
truncateTableAndSetCet_Environment = ''' 
    TRUNCATE table "Stage".Environment;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Environment' 
'''
sourceToStage_Environment = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Environment';

        INSERT INTO "Stage".Environment 
        SELECT * FROM "Source".Environment 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Environment = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Environment' 
'''
##------------------
truncateTableAndSetCet_Drone = ''' 
    TRUNCATE table "Stage".Drone;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Drone' 
'''
sourceToStage_Drone = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Drone';

        INSERT INTO "Stage".Drone 
        SELECT * FROM "Source".Drone 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Drone = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Drone' 
'''
##------------------
truncateTableAndSetCet_DroneInformation = ''' 
    TRUNCATE table "Stage".DroneInformation;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'DroneInformation' 
'''
sourceToStage_DroneInformation = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'DroneInformation';

        INSERT INTO "Stage".DroneInformation 
        SELECT * FROM "Source".DroneInformation 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_DroneInformation = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'DroneInformation' 
'''
##------------------
truncateTableAndSetCet_DroneImage = ''' 
    TRUNCATE table "Stage".DroneImage;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'DroneImage' 
'''
sourceToStage_DroneImage = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'DroneImage';

        INSERT INTO "Stage".DroneImage 
        SELECT * FROM "Source".DroneImage 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_DroneImage = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'DroneImage' 
'''
##------------------
truncateTableAndSetCet_ChargingStation = ''' 
    TRUNCATE table "Stage".ChargingStation;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'ChargingStation' 
'''
sourceToStage_ChargingStation = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'ChargingStation';

        INSERT INTO "Stage".ChargingStation 
        SELECT * FROM "Source".ChargingStation 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_ChargingStation = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'ChargingStation' 
'''
##------------------
truncateTableAndSetCet_ChargingStatus = ''' 
    TRUNCATE table "Stage".ChargingStatus;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'ChargingStatus' 
'''
sourceToStage_ChargingStatus = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'ChargingStatus';

        INSERT INTO "Stage".ChargingStatus 
        SELECT * FROM "Source".ChargingStatus 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_ChargingStatus = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'ChargingStatus' 
'''
##------------------
truncateTableAndSetCet_Task = ''' 
    TRUNCATE table "Stage".Task;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Task' 
'''
sourceToStage_Task = ''' 
    DO $$
    DECLARE 
        Lset1 timestamp; 
        Cet1 timestamp;
    BEGIN
        SELECT Lset, Cet INTO Lset1, Cet1 from "Metadata".data_flow where name = 'Task';

        INSERT INTO "Stage".Task 
        SELECT * FROM "Source".Task 
        where (CreatedDate > Lset1 and CreatedDate < Cet1) or (UpdateDate > Lset1 and UpdateDate < Cet1);
    END $$;
'''
setLset_Task = '''
    UPDATE "Metadata".Data_Flow 
    set Lset = now() where Name = 'Task' 
'''
