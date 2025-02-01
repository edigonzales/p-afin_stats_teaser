DROP TABLE IF EXISTS arbeitslosenzahlen_tmp;
CREATE TEMP TABLE arbeitslosenzahlen_tmp AS 
SELECT 
    * 
FROM 
    read_csv('/Users/stefan/sources/p-afin_stats_teaser/data/arbeitslosenzahlen.csv', header = true)
;

DROP TABLE IF EXISTS arbeitslosenzahlen;
CREATE TEMP TABLE arbeitslosenzahlen AS 
SELECT 
	jahr::int AS jahr,
	Kriterium AS kategorie,
	anzahl
FROM 
(
	UNPIVOT arbeitslosenzahlen_tmp
	ON COLUMNS(* EXCLUDE (Kriterium))
	INTO
	    NAME jahr
	    VALUE anzahl
)
;

COPY arbeitslosenzahlen TO '/Users/stefan/sources/p-afin_stats_teaser/data/ch.so.awa.arbeitslosenzahlen_stellensuchende.csv' (HEADER, DELIMITER ';');

COPY arbeitslosenzahlen TO '/Users/stefan/sources/p-afin_stats_teaser/data/ch.so.awa.arbeitslosenzahlen_stellensuchende.parquet' (FORMAT PARQUET);

INSTALL spatial;
LOAD spatial;
COPY arbeitslosenzahlen TO '/Users/stefan/sources/p-afin_stats_teaser/data/ch.so.awa.arbeitslosenzahlen_stellensuchende.xlsx' WITH (FORMAT GDAL, DRIVER 'xlsx');

