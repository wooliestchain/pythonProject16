-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 09 mai 2023 à 02:16
-- Version du serveur : 10.4.27-MariaDB
-- Version de PHP : 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `wool`
--

-- --------------------------------------------------------

--
-- Structure de la table `commerce`
--

CREATE TABLE `commerce` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `code` int(11) NOT NULL,
  `commerce_name` varchar(255) NOT NULL,
  `year_fond` int(11) NOT NULL,
  `sector` varchar(255) NOT NULL,
  `descr` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `commerce`
--

INSERT INTO `commerce` (`id`, `code`, `commerce_name`, `year_fond`, `sector`, `descr`) VALUES
(1, 0, 'Nom de votre compagnie', 0, 'Secteur', '\n'),
(2, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(3, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(4, 1234, 'nimp', 2022, 'nimp', 'nimp\n'),
(5, 145, 'nimp', 2022, 'nimp', 'nimp\n'),
(6, 0, 'd', 2, 'd', 'd\n'),
(7, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(8, 0, 'dsds', 2, 'dd', 'sdds\n'),
(9, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(10, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(11, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(12, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(13, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(14, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(15, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(16, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(17, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(18, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(19, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(20, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(21, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(22, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(23, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(24, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(25, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(26, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(27, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(28, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(29, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(30, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(31, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(32, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(33, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(34, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(35, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(36, 0, 'eer', 5, 'de', 'ere\n'),
(37, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(38, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(39, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(40, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(41, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(42, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(43, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(44, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(45, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(46, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(47, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(48, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(49, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(50, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(51, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(52, 12, 'ffe', 2002, 'dsd', 'dfddf'),
(53, 12, 'ffe', 2002, 'dsd', 'dfddf');

-- --------------------------------------------------------

--
-- Structure de la table `product`
--

CREATE TABLE `product` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `code` int(255) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_categorie` varchar(255) NOT NULL,
  `prix` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `product`
--

INSERT INTO `product` (`id`, `code`, `product_name`, `product_categorie`, `prix`) VALUES
(1, 0, 'mangue', 'fruit', 10),
(2, 10, 'raisin', 'pépin', 40),
(3, 10, 'raisin', 'pépin', 40),
(4, 10, 'raisin', 'pépin', 40),
(5, 12, 'poire', 'pepin', 20),
(6, 12, 'poire', 'pepin', 20);

-- --------------------------------------------------------

--
-- Structure de la table `sales`
--

CREATE TABLE `sales` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `amount` float NOT NULL,
  `quantity` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT curdate(),
  `year` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `day` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `sales`
--

INSERT INTO `sales` (`id`, `product_name`, `amount`, `quantity`, `date`, `year`, `month`, `day`) VALUES
(1, 'produit_1', 10.99, 3, '2023-04-26', 2023, 4, 26),
(2, 'produit_1', 10.99, 3, '2023-04-26', 2023, 4, 26),
(13, 'produit_1', 10.99, 3, '2023-04-28', 2023, 4, 28),
(14, 'mangue', 20, 5, '2023-04-28', 2023, 4, 28),
(15, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(16, 'peche', 14.99, 5, '2023-04-28', 2023, 4, 28),
(17, 'peche', 14.99, 5, '2023-04-28', 2023, 4, 28),
(18, 'poire', 18.5, 10, '2023-04-28', 2023, 4, 28),
(19, 'orange', 14.8, 15, '2023-04-28', 2023, 4, 28),
(20, 'torche', 20.5, 4, '2023-04-28', 2023, 4, 28),
(21, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(22, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(23, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(24, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(25, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(26, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(27, 'fruit', 15, 3, '2023-04-28', 2023, 4, 28),
(28, 'orange', 15, 15, '2023-05-08', 2023, 5, 8),
(29, 'pomme', 18, 5, '2023-05-08', 2023, 5, 8),
(30, 'fruit', 15, 2, '2023-05-08', 2023, 5, 8),
(31, 'orange', 15, 10, '2023-05-08', 2023, 5, 8),
(32, 'orange', 18, 2, '2023-05-08', 2023, 5, 8);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`) VALUES
(18, 'messi', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(19, 'crist', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(20, 'emma', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(21, 'emmaa', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(22, 'mich', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(23, 'mich1', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(24, 'sam', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(25, 'lab', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(26, 'ney', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(27, 'miss', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(28, 'Username', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', ''),
(29, 'nam', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(30, 'naa', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(31, 'ddf', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(32, 'dsd', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(33, 'ddfd', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(34, 'kart', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(35, 'some', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(36, 'thing', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(37, 'fdff', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(38, 'efeffe', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(39, 'ddffdfd', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(40, 'fdfdff', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(41, 'ddffvf', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(42, 'ffdffd', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(43, 'huh', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(44, 'eererer', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(45, 'eererdfd', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(46, 'jnkn', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', ''),
(47, 'jlk', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `commerce`
--
ALTER TABLE `commerce`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `commerce`
--
ALTER TABLE `commerce`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT pour la table `product`
--
ALTER TABLE `product`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
