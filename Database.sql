CREATE TABLE PROJECT (
  project_name TEXT PRIMARY KEY
);


CREATE TABLE TEST (
  id_test UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name_student TEXT NOT NULL,
  test_date TIMESTAMP NOT NULL DEFAULT NOW(),
  test_name TEXT NOT NULL,
  p_name TEXT NOT NULL,
  FOREIGN KEY (p_name) REFERENCES project(project_name)
);

CREATE TABLE BATTERY (
  id_test UUID PRIMARY KEY,
  name_cell TEXT NOT NULL,
  nom_volt DECIMAL NOT NULL,
  nom_cap DECIMAL NOT NULL,
  current BYTEA NOT NULL,
  timestmp BYTEA NOT NULL,
  voltage BYTEA NOT NULL,
  FOREIGN KEY (id_test) REFERENCES TEST(id_test)
);
