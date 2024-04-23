truncateTableAndSetCet_Country = ''' 
    TRUNCATE table "Stage".Country;

    UPDATE "Metadata".Data_Flow 
    set Cet = now() where Name = 'Country' 
'''
sourceToStage_Country = ''' 
    DOsourceToStage_Country $$
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