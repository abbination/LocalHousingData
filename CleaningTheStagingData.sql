USE HousingDataProject
GO

--Using SQL to clean the data and output a file more friendly for upload into python

SELECT TOP (1000) 
	   CASE [Question1]
		WHEN '' THEN 'No Answer'
		ELSE UPPER(TRIM([Question1])) END AS [Question1]
      ,[Question2]
      ,CASE [Question3]
		WHEN 'No' THEN ''
		WHEN 'Unhioused' THEN 'No Consistent Or Stable Housing'
		WHEN 'UNHOUSED' THEN 'No Consistent Or Stable Housing'
		WHEN 'Have no consistent or stable housing' THEN 'No Consistent Or Stable Housing'
		ELSE UPPER(TRIM([Question3])) END AS [Question3]
      ,CASE [Question4]
		WHEN 'MP' THEN 'NO'
		WHEN 'Rent' THEN ''
		ELSE UPPER(TRIM([Question4])) END AS [Question4]
      ,CASE [Question5]
		WHEN 'Rent' THEN ''
		ELSE UPPER([Question5]) END AS [Question5]
      ,CASE [Question6]
		WHEN 'IDK' THEN 'N/A'
		WHEN 'NA' THEN 'N/A'
		ELSE UPPER([Question6]) END AS [Question6]
      ,UPPER([Question7]) AS [Question7]
      ,CASE [Question8]
		WHEN '?' THEN ''
		ELSE UPPER([Question8]) END AS [Question8]
      ,CASE [Question9]
		WHEN 'NI' THEN 'NO'
		ELSE UPPER([Question9]) END AS [Question9]
      ,CASE [Question10]
		WHEN 'I don''t know' THEN 'IDK'
		ELSE UPPER([Question10]) END AS [Question10]
      ,CASE [Question11]
		WHEN 'I don''t know' THEN 'IDK'
		WHEN 'UDK' THEN 'IDK'
		WHEN 'N0' THEN 'NO'
		ELSE UPPER([Question11]) END AS [Question11]
      ,CASE [Question12]
		WHEN 'NA' THEN 'NO'
		WHEN 'I don''t know' THEN 'IDK'
		ELSE UPPER([Question12]) END AS [Question12]
      ,CASE [Question13]
		WHEN 'NA' THEN 'N/A'
		ELSE UPPER([Question13]) END AS [Question13]
      ,CASE [Question14]
		WHEN 'I don''t know' THEN 'IDK'
		WHEN 'YIDK' THEN 'IDK'
		ELSE UPPER([Question14]) END AS [Question14]
      ,CASE [Question15]
		WHEN '' THEN 'No Answer'
		ELSE UPPER([Question15]) END AS [Question15]
      ,UPPER([Question16a]) AS [Question16a]
      ,[Question16b]
      ,CASE [Question17]
		WHEN '1+4 times' THEN '1-4 times'
		WHEN '1=4 times' THEN '1-4 times'
		WHEN '5+ timed' THEN '5+ times'
		WHEN '5+times' THEN '5+ times'
		WHEN 'Nevery' THEN 'Never'
		WHEN 'NEVER' THEN 'Never'
		WHEN '' THEN 'No Answer'
		ELSE TRIM([Question17]) END AS [Question17]
      ,[Question18]
      ,[Question19]
      ,CASE [Question20]
		WHEN 'MO' THEN 'NO'
		ELSE UPPER(TRIM([Question20])) END AS [Question20]
      ,CASE [Question21]
		WHEN '' THEN 'No Answer'
		ELSE UPPER([Question21]) END AS [Question21]
FROM [staging].[HousingSurvey]




