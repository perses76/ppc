DROP TABLE IF EXISTS kpi1;
DROP TABLE IF EXISTS kpi2;

CREATE TABLE kpi1(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    interval_start_timestamp BIGINT NOT NULL,
    interval_end_timestamp BIGINT NOT NULL,
    service_id INTEGER NOT NULL,
    total_bytes INTEGER NOT NULL,
    `interval` VARCHAR(5) NOT NULL,
    CONSTRAINT chk_kpi1_interval CHECK (`interval` in ('5min', '1h'))
);


CREATE TABLE kpi2(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    interval_start_timestamp BIGINT NOT NULL,
    interval_end_timestamp BIGINT NOT NULL,
    cell_id INTEGER NOT NULL,
    number_of_unique_users INT NOT NULL,
    `interval` VARCHAR(5) NOT NULL,
    CONSTRAINT chk_kpi1_interval CHECK (`interval` in ('5min', '1h'))
);
