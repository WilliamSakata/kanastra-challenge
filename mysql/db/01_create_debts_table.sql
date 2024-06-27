CREATE TABLE debts (
    `id` VARCHAR(36) NOT NULL,
    `due_date` VARCHAR(10) NOT NULL,
    `payer_id` INT(11) NOT NULL,
    `amount` DECIMAL(10,2) NOT NULL,
    `dat_created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`payer_id`) REFERENCES payers(`id`)
)