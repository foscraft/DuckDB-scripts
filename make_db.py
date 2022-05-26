import duckdb

conn = duckdb.connect("insurance.duckdb")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE insurance(
  policyID          int 
  ,statecode         varchar 
  ,county           varchar
  ,eq_site_limit    bigint
  ,hu_site_limit    bigint  
  ,point_atitude         double 
  ,point_longitude        double 
  ,line             varchar 
  ,construction       varchar
)
"""
)

cursor.execute("COPY insurance FROM 'data/insurance.csv' (HEADER)")

print(cursor.execute("select count(*) from insurance").fetchall())
cursor.close()
conn.close()
