# SoftCart MongoDB NoSQL Catalog Database

All of SoftCart's catalog data will be stored on a MongoDB NoSQL server. This README provides step-by-step instructions to create the database `catalog`, import our electronics products from `catalog.json` into a collection named `electronics`, run test queries against the data, and export the collection into a file named `electronics.csv` using only the `_id`, `type`, and `model` fields.

## 1. Install Dependencies

This assignment uses `mongoimport` and `mongoexport` commands from the MongoDB CLI Database Tools library. 

### Check for MongoDB CLI Tools

First, check if the MongoDB CLI tools are installed by running:

```bash
mongoimport

You should see an output similar to:
2023-02-05T15:11:01.000-0500    no collection specified
2023-02-05T15:11:01.000-0500    using filename '' as collection
2023-02-05T15:11:01.000-0500    error validating settings: invalid collection name: collection name cannot be an empty string
```


## 2. Import Catalog Data From JSON

Ensure MongoDB is running:

```bash
sudo service mongodb start
```

### Create Database and Collection

### Import Catalog Data

Download the catalog data (`catalog.json`) using `wget`:

```bash
sudo wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json
```

Use `mongoimport` to import the downloaded JSON data into the `electronics` collection of the `catalog` database. Replace `PASSWORD` with your MongoDB password:

```bash
mongoimport -u root --authenticationDatabase admin -p PASSWORD --db catalog --file catalog.json
```

You should see output similar to:

```text
2023-02-05T16:31:01.726-0500    connected to: mongodb://localhost/
2023-02-05T16:31:01.751-0500    438 document(s) imported successfully. 0 document(s) failed to import.
```

This completes the import of catalog data into MongoDB.




## 3. Run Test Queries

### Display List of Databases

To display a list of all databases, use the following command in the MongoDB CLI:

```bash
show dbs
```

You should see output similar to:

```text
admin       80.00 KiB
catalog      40.00 KiB
config        12.000 KiB
local            64.00 KiB
```

### Display List of Collections

To display a list of all collections in the `catalog` database, use the following commands:

```bash
use catalog
show collections
```

You should see:

```text
electronics
```

This confirms that the `electronics` collection exists in your `catalog` database.



## 4. Create Index and Run Test Queries

### Create Index

To create an index for the `type` field in the `electronics` collection, use the following command in the MongoDB CLI:

```bash
mongo
use catalog
db.electronics.createIndex({"type": 1})
```

You should see output similar to:

```text
{
  "createdCollectionAutomatically" : false,
  "numIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}
```

### Run Test Queries

Now that our collection is indexed, let's run a few test queries:

#### Display Record Count for Product Type Laptops

To display the record count for product type laptops:

```bash
db.electronics.count({"type": "laptop"})
```

You should see:

```text
389
```

#### Display Record Count for Product Type Smartphones with Screen Size 6

To display the record count for product type smartphones with a screen size of 6:

```bash
db.electronics.count({"type": "smart phone", "screen size": 6})
```

You should see:

```text
24
```

#### Aggregate Query to Calculate Average Screen Size of Smartphones

To calculate the average screen size of product type smartphones:

```bash
db.electronics.aggregate([
    { $match: { "type": "smart phone" } },
    { $group: { _id: "$type", average: { $avg: "$screen size" } } }
])
```

You should see output similar to:

```text
{ "_id" : "smart phone", "average" : 6 }
```

This completes the index creation and test queries section for the `electronics` collection in your MongoDB database.



## 5. Export Data to CSV

To export the `electronics` collection into a CSV file named `electronics.csv` with only the `_id`, `type`, and `model` columns, use the following command in the MongoDB CLI:

```bash
mongoexport -u root --authenticationDatabase admin -p PASSWORD --db catalog --collection electronics --fields _id,type,model --type=csv --out electronics.csv
```

You should see output similar to:

```text
2024-06-25T07:58:46.094-0400    connected to: mongodb://localhost/
2024-06-25T07:58:46.104-0400    exported 438 records
```

This command exports 438 records from the `electronics` collection into a CSV file named `electronics.csv` in your current working directory.

This completes the export data section for your MongoDB `electronics` collection.

