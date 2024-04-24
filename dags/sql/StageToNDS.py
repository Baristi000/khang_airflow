StageToNDS_Country = ''' 
    MERGE INTO "NDS".country AS t1
    USING "Stage".country AS t2
    ON (t1.CountryID = t2.CountryID)
    WHEN MATCHED THEN
        UPDATE SET
            CountryName = t2.CountryName,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (CountryID, CountryName, CreatedDate, UpdateDate)
        VALUES (t2.CountryID, t2.CountryName, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Region = ''' 
    MERGE INTO "NDS".Region AS t1
    USING (select * from "Stage".Region 
	    where "Stage".Region.countryid in (select countryid from "NDS".Country)) AS t2
    ON (t1.RegionID = t2.RegionID)
    WHEN MATCHED THEN
        UPDATE SET
            CountryID = t2.CountryID,
            RegionName = t2.RegionName,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (RegionID, CountryID, RegionName, CreatedDate, UpdateDate)
        VALUES (t2.RegionID, t2.CountryID, t2.RegionName, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Address = ''' 
    MERGE INTO "NDS".Address AS t1
    USING (select * from "Stage".Address 
	    where "Stage".Address.RegionID in (select RegionID from "NDS".Region)) AS t2
    ON (t1.AddressID = t2.AddressID)
    WHEN MATCHED THEN
        UPDATE SET
            RegionID = t2.RegionID,
            City = t2.City,
            AddressLine = t2.AddressLine,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (AddressID, RegionID, City, AddressLine, CreatedDate, UpdateDate)
        VALUES (t2.AddressID, t2.RegionID, t2.City, t2.AddressLine, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Account = ''' 
    MERGE INTO "NDS".Account AS t1
    USING "Stage".Account AS t2
    ON (t1.AccountID = t2.AccountID)
    WHEN MATCHED THEN
        UPDATE SET
            Username = t2.Username,
            Password = t2.Password,
            Role = t2.Role,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (AccountID, Username, Password, Role, CreatedDate, UpdateDate)
        VALUES (t2.AccountID, t2.Username, t2.Password, t2.Role, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_UserInfo = ''' 
    MERGE INTO "NDS".UserInfo AS t1
    USING (select * from "Stage".UserInfo 
	    where ("Stage".UserInfo.AddressID in (select AddressID from "NDS".Address))
        and ("Stage".UserInfo.AccountID in (select AccountID from "NDS".Account)) ) AS t2
    ON (t1.UserID = t2.UserID)
    WHEN MATCHED THEN
        UPDATE SET
            FirstName = t2.FirstName,
            LastName = t2.LastName,
            Gender = t2.Gender,
            DateOfBirth = t2.DateOfBirth,
            AddressID = t2.AddressID,
            AccountID = t2.AccountID,
            Email = t2.Email,
            PhoneNumber = t2.PhoneNumber,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (UserID, FirstName, LastName, Gender, DateOfBirth, AddressID, AccountID, Email, PhoneNumber, CreatedDate, UpdateDate)
        VALUES (t2.UserID, t2.FirstName, t2.LastName, t2.Gender, t2.DateOfBirth, t2.AddressID, t2.AccountID, t2.Email, t2.PhoneNumber, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Field = ''' 
    MERGE INTO "NDS".Field AS t1
    USING (select * from "Stage".Field 
	    where "Stage".Field.RegionID in (select RegionID from "NDS".Region)) AS t2
    ON (t1.FieldID = t2.FieldID)
    WHEN MATCHED THEN
        UPDATE SET
            RegionID = t2.RegionID,
            FieldName = t2.FieldName,
            Area = t2.Area,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (FieldID, RegionID, FieldName, Area, CreatedDate, UpdateDate)
        VALUES (t2.FieldID, t2.RegionID, t2.FieldName, t2.Area, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_RubberTree = ''' 
    MERGE INTO "NDS".RubberTree AS t1
    USING (select * from "Stage".RubberTree 
	    where "Stage".RubberTree.FieldID in (select FieldID from "NDS".Field)) AS t2
    ON (t1.TreeID = t2.TreeID)
    WHEN MATCHED THEN
        UPDATE SET
            FieldID = t2.FieldID,
            Location = t2.Location,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (TreeID, FieldID, Location, CreatedDate, UpdateDate)
        VALUES (t2.TreeID, t2.FieldID, t2.Location, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_RubberTreeInformation = ''' 
    MERGE INTO "NDS".TreeInfo AS t1
    USING (select * from "Stage".TreeInfo 
	    where "Stage".TreeInfo.TreeID in (select TreeID from "NDS".RubberTree)) AS t2
    ON (t1.TreeInfoID = t2.TreeInfoID)
    WHEN MATCHED THEN
        UPDATE SET
            TreeID = t2.TreeID,
            TopHeight = t2.TopHeight,
            CrownHeight = t2.CrownHeight,
            Diameter = t2.Diameter,
            Circumference = t2.Circumference,
            CheckDate = t2.CheckDate,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (TreeInfoID, TreeID, TopHeight, CrownHeight, Diameter, Circumference, CheckDate, CreatedDate, UpdateDate)
        VALUES (t2.TreeInfoID, t2.TreeID, t2.TopHeight, t2.CrownHeight, t2.Diameter, t2.Circumference, t2.CheckDate, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Plan = ''' 
    MERGE INTO "NDS".Plan AS t1
    USING "Stage".Plan AS t2
    ON (t1.PlanID = t2.PlanID)
    WHEN MATCHED THEN
        UPDATE SET
            Name = t2.Name,
            Description = t2.Description,
            StartDate = t2.StartDate,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (PlanID, Name, Description, StartDate, CreatedDate, UpdateDate)
        VALUES (t2.PlanID, t2.Name, t2.Description, t2.StartDate, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_PlanDetail = ''' 
    MERGE INTO "NDS".PlanDetail AS t1
    USING (select * from "Stage".PlanDetail 
	    where ("Stage".PlanDetail.fieldID in (select fieldID from "NDS".Field))
        and ("Stage".PlanDetail.PlanID in (select PlanID from "NDS".Plan)) ) AS t2
    ON (t1.FieldID = t2.FieldID and t1.PlanID = t2.PlanID)
    WHEN MATCHED THEN
        UPDATE SET
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (FieldID, PlanID, CreatedDate, UpdateDate)
        VALUES (t2.FieldID, t2.PlanID, t2.CreatedDate, t2.UpdateDate);
'''

StageToNDS_Lidar = ''' 
    MERGE INTO "NDS".Lidar AS t1
    USING "Stage".Lidar AS t2
    ON (t1.LidarID = t2.LidarID)
    WHEN MATCHED THEN
        UPDATE SET
            Model = t2.Model,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (LidarID, Model, CreatedDate, UpdateDate)
        VALUES (t2.LidarID, t2.Model, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Camera = ''' 
    MERGE INTO "NDS".Camera AS t1
    USING "Stage".Camera AS t2
    ON (t1.CameraID = t2.CameraID)
    WHEN MATCHED THEN
        UPDATE SET
            Model = t2.Model,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (CameraID, Model, CreatedDate, UpdateDate)
        VALUES (t2.CameraID, t2.Model, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Radar = ''' 
    MERGE INTO "NDS".Radar AS t1
    USING "Stage".Radar AS t2
    ON (t1.RadarID = t2.RadarID)
    WHEN MATCHED THEN
        UPDATE SET
            Model = t2.Model,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (RadarID, Model, CreatedDate, UpdateDate)
        VALUES (t2.RadarID, t2.Model, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_SensorControlSystem = ''' 
    MERGE INTO "NDS".SensorControlSystem AS t1
    USING (select * from "Stage".SensorControlSystem 
	    where ("Stage".SensorControlSystem.LidarID in (select LidarID from "NDS".Lidar))
        and ("Stage".SensorControlSystem.CameraID in (select CameraID from "NDS".Camera))
        and ("Stage".SensorControlSystem.RadarID in (select RadarID from "NDS".Radar)) ) AS t2
    ON (t1.ScsID = t2.ScsID)
    WHEN MATCHED THEN
        UPDATE SET
            LidarID = t2.LidarID,
            CameraID = t2.CameraID,
            RadarID = t2.RadarID,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (ScsID, LidarID, CameraID, RadarID, CreatedDate, UpdateDate)
        VALUES (t2.ScsID, t2.LidarID, t2.CameraID, t2.RadarID, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Robot = ''' 
    MERGE INTO "NDS".Robot AS t1
    USING "Stage".Robot AS t2
    ON (t1.RobotID = t2.RobotID)
    WHEN MATCHED THEN
        UPDATE SET
            TypeRobot = t2.TypeRobot,
            Model = t2.Model,
            Status = t2.Status,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (RobotID, TypeRobot, Model, Status, CreatedDate, UpdateDate)
        VALUES (t2.RobotID, t2.TypeRobot, t2.Model, t2.Status, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Energy = ''' 
    MERGE INTO "NDS".Energy AS t1
    USING (select * from "Stage".Energy 
	    where "Stage".Energy.RobotID in (select RobotID from "NDS".Robot)) AS t2
    ON (t1.EnergyID = t2.EnergyID)
    WHEN MATCHED THEN
        UPDATE SET
            RobotID = t2.RobotID,
            RemainingTime = t2.RemainingTime,
            RemainingEnergy = t2.RemainingEnergy,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (EnergyID, RobotID, RemainingTime, RemainingEnergy, CreatedDate, UpdateDate)
        VALUES (t2.EnergyID, t2.RobotID, t2.RemainingTime, t2.RemainingEnergy, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_RobotTapping = ''' 
    MERGE INTO "NDS".RobotTapping AS t1
    USING (select * from "Stage".RobotTapping 
	    where ("Stage".RobotTapping.RobotID in (select RobotID from "NDS".Robot))
        and ("Stage".RobotTapping.TreeID in (select TreeID from "NDS".RubberTree)) ) AS t2
    ON (t1.RobotTappingID = t2.RobotTappingID)
    WHEN MATCHED THEN
        UPDATE SET
            RobotID = t2.RobotID,
            TreeID = t2.TreeID,
            Direction = t2.Direction,
            Speed = t2.Speed,
            Quantity = t2.Quantity,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (RobotTappingID, RobotID, TreeID, Direction, Speed, Quantity, CreatedDate, UpdateDate)
        VALUES (t2.RobotTappingID, t2.RobotID, t2.TreeID, t2.Direction, t2.Speed, t2.Quantity, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Blade = ''' 
    MERGE INTO "NDS".Blade AS t1
    USING (select * from "Stage".Blade 
	    where "Stage".Blade.RobotTappingID in (select RobotTappingID from "NDS".RobotTapping)) AS t2
    ON (t1.BladeID = t2.BladeID)
    WHEN MATCHED THEN
        UPDATE SET
            RobotTappingID = t2.RobotTappingID,
            TappingStatus = t2.TappingStatus,
            Angle = t2.Angle,
            Depth = t2.Depth,
            BladeStatus = t2.BladeStatus,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (BladeID, RobotTappingID, TappingStatus, Angle, Depth, BladeStatus, CreatedDate, UpdateDate)
        VALUES (t2.BladeID, t2.RobotTappingID, t2.TappingStatus, t2.Angle, t2.Depth, t2.BladeStatus, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Environment = ''' 
    MERGE INTO "NDS".Environment AS t1
    USING (select * from "Stage".Environment 
	    where "Stage".Environment.RobotTappingID in (select RobotTappingID from "NDS".RobotTapping)) AS t2
    ON (t1.EnvironmentID = t2.EnvironmentID)
    WHEN MATCHED THEN
        UPDATE SET
            RobotTappingID = t2.RobotTappingID,
            WindDirection = t2.WindDirection,
            WindSpeed = t2.WindSpeed,
            Temperature = t2.Temperature,
            Rainfall = t2.Rainfall,
            Time = t2.Time,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (EnvironmentID, RobotTappingID, WindDirection, WindSpeed, Temperature, Rainfall, Time, CreatedDate, UpdateDate)
        VALUES (t2.EnvironmentID, t2.RobotTappingID, t2.WindDirection, t2.WindSpeed, t2.Temperature, t2.Rainfall, t2.Time, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Drone = ''' 
    MERGE INTO "NDS".Drone AS t1
    USING (select * from "Stage".Drone 
	    where ("Stage".Drone.RobotID in (select RobotID from "NDS".Robot))
        and ("Stage".Drone.ScsID in (select ScsID from "NDS".SensorControlSystem)) ) AS t2
    ON (t1.DroneID = t2.DroneID)
    WHEN MATCHED THEN
        UPDATE SET
            RobotID = t2.RobotID,
            ScsID = t2.ScsID,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (DroneID, RobotID, ScsID, CreatedDate, UpdateDate)
        VALUES (t2.DroneID, t2.RobotID, t2.ScsID, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_DroneInformation = ''' 
    MERGE INTO "NDS".DroneInformation AS t1
    USING (select * from "Stage".DroneInformation 
	    where "Stage".DroneInformation.DroneID in (select DroneID from "NDS".Drone)) AS t2
    ON (t1.DroneInfoID = t2.DroneInfoID)
    WHEN MATCHED THEN
        UPDATE SET
            DroneID = t2.DroneID,
            Direction = t2.Direction,
            Speed = t2.Speed,
            Height = t2.Height,
            CurrentLocation = t2.CurrentLocation,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (DroneInfoID, DroneID, Direction, Speed, Height, CurrentLocation, CreatedDate, UpdateDate)
        VALUES (t2.DroneInfoID, t2.DroneID, t2.Direction, t2.Speed, t2.Height, t2.CurrentLocation, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_DroneImage = ''' 
    MERGE INTO "NDS".DroneImage AS t1
    USING (select * from "Stage".DroneImage 
	    where ("Stage".DroneImage.DroneID in (select DroneID from "NDS".Drone))
        and ("Stage".DroneImage.TreeID in (select TreeID from "NDS".RubberTree)) ) AS t2
    ON (t1.DroneImageID = t2.DroneImageID)
    WHEN MATCHED THEN
        UPDATE SET
            DroneID = t2.DroneID,
            TreeID = t2.TreeID,
            Image = t2.Image,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (DroneImageID, DroneID, TreeID, Image, CreatedDate, UpdateDate)
        VALUES (t2.DroneImageID, t2.DroneID, t2.TreeID, t2.Image, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_ChargingStation = ''' 
    MERGE INTO "NDS".ChargingStation AS t1
    USING "Stage".ChargingStation AS t2
    ON (t1.ChargingStationID = t2.ChargingStationID)
    WHEN MATCHED THEN
        UPDATE SET
            Location = t2.Location,
            MaxRobotNumber = t2.MaxRobotNumber,
            CurrentRobotNumber = t2.CurrentRobotNumber,
            Status = t2.Status,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (ChargingStationID, Location, MaxRobotNumber, CurrentRobotNumber, Status, CreatedDate, UpdateDate)
        VALUES (t2.ChargingStationID, t2.Location, t2.MaxRobotNumber, t2.CurrentRobotNumber, t2.Status, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_ChargingStatus = ''' 
    MERGE INTO "NDS".ChargingStatus AS t1
    USING (select * from "Stage".ChargingStatus 
	    where ("Stage".ChargingStatus.RobotID in (select RobotID from "NDS".Robot))
        and ("Stage".ChargingStatus.ChargingStationID in (select ChargingStationID from "NDS".RubberChargingStation)) ) AS t2
    ON (t1.ChargingStatusID = t2.ChargingStatusID)
    WHEN MATCHED THEN
        UPDATE SET
            DroneID = t2.DroneID,
            ChargingStationID = t2.ChargingStationID,
            CurrentBattery = t2.CurrentBattery,
            Status = t2.Status,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (ChargingStatusID, DroneID, ChargingStationID, CurrentBattery, Status, CreatedDate, UpdateDate)
        VALUES (t2.ChargingStatusID, t2.DroneID, t2.ChargingStationID, t2.CurrentBattery, t2.Status, t2.CreatedDate, t2.UpdateDate);   
'''

StageToNDS_Task = ''' 
    MERGE INTO "NDS".Task AS t1
    USING "Stage".Task AS t2
    USING (select * from "Stage".Task 
	    where ("Stage".Task.RobotID in (select RobotID from "NDS".Robot))
        and ("Stage".Task.PlanID in (select PlanID from "NDS".RubberPlan)) ) AS t2
    ON (t1.TaskID = t2.TaskID)
    WHEN MATCHED THEN
        UPDATE SET
            RobotID = t2.RobotID,
            PlanID = t2.PlanID,
            ActionDetail = t2.ActionDetail,
            UpdateDate = t2.UpdateDate
    WHEN NOT MATCHED THEN
        INSERT (TaskID, RobotID, PlanID, ActionDetail, CreatedDate, UpdateDate)
        VALUES (t2.TaskID, t2.RobotID, t2.PlanID, t2.ActionDetail, t2.CreatedDate, t2.UpdateDate);   
'''