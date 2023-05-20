

CREATE TABLE `mint_package` (
  `id` int(11) NOT NULL,
  `mintWallet` varchar(63) NOT NULL,
  `priceOfSaleEth` decimal(5,2) NOT NULL,
  `pricePaidEth` decimal(5,2) NOT NULL,
  `mintAt` datetime NOT NULL,
  `tokens` varchar(255) NOT NULL,
  `nbTokens` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `mint_package`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `mint_package`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
