
-- Funktioniert erst mit 1.1.4
--SELECT * FROM read_csv('/Users/stefan/sources/p-afin_stats_teaser/data/Fahrzeugbestand_SO_24_MFK_latin1.csv', encoding='latin-1');


DROP TABLE IF EXISTS fahrzeugbestand_2024_tmp;
CREATE TEMP TABLE fahrzeugbestand_2024_tmp AS 
SELECT 
    * 
FROM 
    read_csv('/Users/stefan/sources/p-afin_stats_teaser/data/Fahrzeugbestand_SO_24_MFK_utf8.csv')
;

DROP TABLE IF EXISTS fahrzeugbestand_tmp;
CREATE TEMP TABLE fahrzeugbestand_tmp AS  
SELECT 
    2024 AS jahr,
    replace(Bezirk, 'Bezirk ', '') AS bezirk,
    Kanton AS kanton,
    typ,
    anzahl
FROM 
(
    UNPIVOT fahrzeugbestand_2024_tmp
    ON COLUMNS(* EXCLUDE (Bezirk, Kanton))
    INTO
        NAME typ
        VALUE anzahl
)

UNION ALL 

SELECT 
    jahr::int,
    replace(bezirk, 'Bezirk ', '') AS bezirk,
    kanton,
    typ,
    anzahl
FROM 
    read_csv('/Users/stefan/sources/p-afin_stats_teaser/data/fahrzeugbestand_1990-2023.csv')
WHERE
    jahr != 1990    
ORDER BY 
    jahr, bezirk, typ
;

COPY fahrzeugbestand_tmp TO '/Users/stefan/sources/p-afin_stats_teaser/data/ch.so.mfk.fahrzeugbestand_1990-2024.csv' (HEADER, DELIMITER ';');

COPY fahrzeugbestand_tmp TO '/Users/stefan/sources/p-afin_stats_teaser/data/ch.so.mfk.fahrzeugbestand_1990-2024.parquet' (FORMAT PARQUET);

INSTALL spatial;
LOAD spatial;
COPY fahrzeugbestand_tmp TO '/Users/stefan/sources/p-afin_stats_teaser/data/ch.so.mfk.fahrzeugbestand_1990-2024.xlsx' WITH (FORMAT GDAL, DRIVER 'xlsx');





