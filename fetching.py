import duckdb

conn = duckdb.connect("insurance.duckdb")
cursor = conn.cursor()


query = "select policyID,statecode,county,eq_site_limit,hu_site_limit from insurance"
print(cursor.execute(query).fetchdf())