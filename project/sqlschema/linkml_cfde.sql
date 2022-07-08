

CREATE TABLE analysis_type (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE anatomy (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE assay_type (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE biosample (
	id_namespace TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	project_id_namespace TEXT NOT NULL, 
	project_local_id TEXT NOT NULL, 
	persistent_id TEXT, 
	creation_time DATETIME, 
	assay_type TEXT, 
	anatomy TEXT, 
	PRIMARY KEY (id_namespace, local_id, project_id_namespace, project_local_id, persistent_id, creation_time, assay_type, anatomy)
);

CREATE TABLE biosample_disease (
	biosample_id_namespace TEXT NOT NULL, 
	biosample_local_id TEXT NOT NULL, 
	association_type VARCHAR(1) NOT NULL, 
	disease TEXT NOT NULL, 
	PRIMARY KEY (biosample_id_namespace, biosample_local_id, association_type, disease)
);

CREATE TABLE biosample_from_subject (
	biosample_id_namespace TEXT NOT NULL, 
	biosample_local_id TEXT NOT NULL, 
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	age_at_sampling TEXT, 
	PRIMARY KEY (biosample_id_namespace, biosample_local_id, subject_id_namespace, subject_local_id, age_at_sampling)
);

CREATE TABLE biosample_gene (
	biosample_id_namespace TEXT NOT NULL, 
	biosample_local_id TEXT NOT NULL, 
	gene TEXT NOT NULL, 
	PRIMARY KEY (biosample_id_namespace, biosample_local_id, gene)
);

CREATE TABLE biosample_in_collection (
	biosample_id_namespace TEXT NOT NULL, 
	biosample_local_id TEXT NOT NULL, 
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	PRIMARY KEY (biosample_id_namespace, biosample_local_id, collection_id_namespace, collection_local_id)
);

CREATE TABLE biosample_substance (
	biosample_id_namespace TEXT NOT NULL, 
	biosample_local_id TEXT NOT NULL, 
	substance TEXT NOT NULL, 
	PRIMARY KEY (biosample_id_namespace, biosample_local_id, substance)
);

CREATE TABLE collection (
	id_namespace TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	persistent_id TEXT, 
	creation_time DATETIME, 
	abbreviation TEXT, 
	description TEXT, 
	has_time_series_data BOOLEAN, 
	PRIMARY KEY (id_namespace, local_id, persistent_id, creation_time, abbreviation, description, has_time_series_data)
);

CREATE TABLE collection_anatomy (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	anatomy TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, anatomy)
);

CREATE TABLE collection_compound (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	compound TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, compound)
);

CREATE TABLE collection_defined_by_project (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	project_id_namespace TEXT NOT NULL, 
	project_local_id TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, project_id_namespace, project_local_id)
);

CREATE TABLE collection_disease (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	disease TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, disease)
);

CREATE TABLE collection_gene (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	gene TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, gene)
);

CREATE TABLE collection_in_collection (
	superset_collection_id_namespace TEXT NOT NULL, 
	superset_collection_local_id TEXT NOT NULL, 
	subset_collection_id_namespace TEXT NOT NULL, 
	subset_collection_local_id TEXT NOT NULL, 
	PRIMARY KEY (superset_collection_id_namespace, superset_collection_local_id, subset_collection_id_namespace, subset_collection_local_id)
);

CREATE TABLE collection_phenotype (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	phenotype TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, phenotype)
);

CREATE TABLE collection_protein (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	protein TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, protein)
);

CREATE TABLE collection_substance (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	substance TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, substance)
);

CREATE TABLE collection_taxonomy (
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	taxon TEXT NOT NULL, 
	PRIMARY KEY (collection_id_namespace, collection_local_id, taxon)
);

CREATE TABLE compound (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE data_type (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE dcc (
	id TEXT NOT NULL, 
	dcc_name TEXT NOT NULL, 
	dcc_abbreviation TEXT NOT NULL, 
	dcc_description TEXT, 
	contact_email TEXT NOT NULL, 
	contact_name TEXT NOT NULL, 
	dcc_url TEXT NOT NULL, 
	project_id_namespace TEXT NOT NULL, 
	project_local_id TEXT NOT NULL, 
	PRIMARY KEY (id, dcc_name, dcc_abbreviation, dcc_description, contact_email, contact_name, dcc_url, project_id_namespace, project_local_id)
);

CREATE TABLE disease (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE file (
	id_namespace TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	project_id_namespace TEXT NOT NULL, 
	project_local_id TEXT NOT NULL, 
	persistent_id TEXT, 
	creation_time DATETIME, 
	size_in_bytes INTEGER, 
	uncompressed_size_in_bytes INTEGER, 
	sha256 TEXT, 
	md5 TEXT, 
	filename TEXT, 
	file_format TEXT, 
	compression_format TEXT, 
	data_type TEXT, 
	assay_type TEXT, 
	analysis_type TEXT, 
	mime_type TEXT, 
	bundle_collection_id_namespace TEXT, 
	bundle_collection_local_id TEXT, 
	dbgap_study_id TEXT, 
	PRIMARY KEY (id_namespace, local_id, project_id_namespace, project_local_id, persistent_id, creation_time, size_in_bytes, uncompressed_size_in_bytes, sha256, md5, filename, file_format, compression_format, data_type, assay_type, analysis_type, mime_type, bundle_collection_id_namespace, bundle_collection_local_id, dbgap_study_id)
);

CREATE TABLE file_describes_biosample (
	file_id_namespace TEXT NOT NULL, 
	file_local_id TEXT NOT NULL, 
	biosample_id_namespace TEXT NOT NULL, 
	biosample_local_id TEXT NOT NULL, 
	PRIMARY KEY (file_id_namespace, file_local_id, biosample_id_namespace, biosample_local_id)
);

CREATE TABLE file_describes_collection (
	file_id_namespace TEXT NOT NULL, 
	file_local_id TEXT NOT NULL, 
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	PRIMARY KEY (file_id_namespace, file_local_id, collection_id_namespace, collection_local_id)
);

CREATE TABLE file_describes_subject (
	file_id_namespace TEXT NOT NULL, 
	file_local_id TEXT NOT NULL, 
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	PRIMARY KEY (file_id_namespace, file_local_id, subject_id_namespace, subject_local_id)
);

CREATE TABLE file_format (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE file_in_collection (
	file_id_namespace TEXT NOT NULL, 
	file_local_id TEXT NOT NULL, 
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	PRIMARY KEY (file_id_namespace, file_local_id, collection_id_namespace, collection_local_id)
);

CREATE TABLE gene (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	organism TEXT NOT NULL, 
	PRIMARY KEY (id, description, synonyms, organism)
);

CREATE TABLE id_namespace (
	id TEXT NOT NULL, 
	abbreviation TEXT, 
	description TEXT, 
	PRIMARY KEY (id, abbreviation, description)
);

CREATE TABLE ncbi_taxonomy (
	id TEXT NOT NULL, 
	clade TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, clade, description, synonyms)
);

CREATE TABLE phenotype (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (id, description, synonyms)
);

CREATE TABLE phenotype_disease (
	phenotype TEXT NOT NULL, 
	disease TEXT NOT NULL, 
	PRIMARY KEY (phenotype, disease)
);

CREATE TABLE phenotype_gene (
	phenotype TEXT NOT NULL, 
	gene TEXT NOT NULL, 
	PRIMARY KEY (phenotype, gene)
);

CREATE TABLE project (
	id_namespace TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	persistent_id TEXT, 
	creation_time DATETIME, 
	abbreviation TEXT, 
	description TEXT, 
	PRIMARY KEY (id_namespace, local_id, persistent_id, creation_time, abbreviation, description)
);

CREATE TABLE project_in_project (
	parent_project_id_namespace TEXT NOT NULL, 
	parent_project_local_id TEXT NOT NULL, 
	child_project_id_namespace TEXT NOT NULL, 
	child_project_local_id TEXT NOT NULL, 
	PRIMARY KEY (parent_project_id_namespace, parent_project_local_id, child_project_id_namespace, child_project_local_id)
);

CREATE TABLE protein (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	organism TEXT, 
	PRIMARY KEY (id, description, synonyms, organism)
);

CREATE TABLE protein_gene (
	protein TEXT NOT NULL, 
	gene TEXT NOT NULL, 
	PRIMARY KEY (protein, gene)
);

CREATE TABLE subject (
	id_namespace TEXT NOT NULL, 
	local_id TEXT NOT NULL, 
	project_id_namespace TEXT NOT NULL, 
	project_local_id TEXT NOT NULL, 
	persistent_id TEXT, 
	creation_time DATETIME, 
	granularity VARCHAR(1) NOT NULL, 
	sex VARCHAR(1), 
	ethnicity VARCHAR(1), 
	age_at_enrollment TEXT, 
	PRIMARY KEY (id_namespace, local_id, project_id_namespace, project_local_id, persistent_id, creation_time, granularity, sex, ethnicity, age_at_enrollment)
);

CREATE TABLE subject_disease (
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	association_type VARCHAR(1) NOT NULL, 
	disease TEXT NOT NULL, 
	PRIMARY KEY (subject_id_namespace, subject_local_id, association_type, disease)
);

CREATE TABLE subject_in_collection (
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	collection_id_namespace TEXT NOT NULL, 
	collection_local_id TEXT NOT NULL, 
	PRIMARY KEY (subject_id_namespace, subject_local_id, collection_id_namespace, collection_local_id)
);

CREATE TABLE subject_phenotype (
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	association_type VARCHAR(1) NOT NULL, 
	phenotype TEXT NOT NULL, 
	PRIMARY KEY (subject_id_namespace, subject_local_id, association_type, phenotype)
);

CREATE TABLE subject_race (
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	race VARCHAR(1), 
	PRIMARY KEY (subject_id_namespace, subject_local_id, race)
);

CREATE TABLE subject_role_taxonomy (
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	role_id VARCHAR(1) NOT NULL, 
	taxonomy_id TEXT NOT NULL, 
	PRIMARY KEY (subject_id_namespace, subject_local_id, role_id, taxonomy_id)
);

CREATE TABLE subject_substance (
	subject_id_namespace TEXT NOT NULL, 
	subject_local_id TEXT NOT NULL, 
	substance TEXT NOT NULL, 
	PRIMARY KEY (subject_id_namespace, subject_local_id, substance)
);

CREATE TABLE substance (
	id TEXT NOT NULL, 
	description TEXT, 
	synonyms TEXT, 
	compound TEXT NOT NULL, 
	PRIMARY KEY (id, description, synonyms, compound)
);
