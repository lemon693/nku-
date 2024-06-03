/*
 Navicat MySQL Dump SQL

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 80036 (8.0.36)
 Source Host           : localhost:3306
 Source Schema         : gamemanager

 Target Server Type    : MySQL
 Target Server Version : 80036 (8.0.36)
 File Encoding         : 65001

 Date: 01/06/2024 16:12:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for a
-- ----------------------------
DROP TABLE IF EXISTS `a`;
CREATE TABLE `a`  (
  `ANO` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ANAME` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `PSWD` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`ANO`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of a
-- ----------------------------
INSERT INTO `a` VALUES ('A1', 'cs', '1');
INSERT INTO `a` VALUES ('A2', 'genshin', '2');
INSERT INTO `a` VALUES ('A3', 'honor', '3');
INSERT INTO `a` VALUES ('A4', 'zmxy', '4');

-- ----------------------------
-- Table structure for p
-- ----------------------------
DROP TABLE IF EXISTS `p`;
CREATE TABLE `p`  (
  `PNO` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `PNAME` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `SEX` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `AGE` tinyint NOT NULL,
  `ELEMENT` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `PSWD` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`PNO`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of p
-- ----------------------------
INSERT INTO `p` VALUES ('P2210001', '穆甲朝', '男', 19, 'cs', '1');
INSERT INTO `p` VALUES ('P2210002', '穆乙朝', '男', 22, 'honor', '2');
INSERT INTO `p` VALUES ('P2210003', '李北雨', '男', 20, 'genshin', '3');
INSERT INTO `p` VALUES ('P2210004', '李西雨', '男', 20, 'genshin', '4');
INSERT INTO `p` VALUES ('P2210006', '邵二航', '男', 21, 'genshin', '6');
INSERT INTO `p` VALUES ('P2210007', '邵三航', '男', 20, '082427', '7');
INSERT INTO `p` VALUES ('P2210008', '穆丙晚', '女', 18, 'cs', '8');
INSERT INTO `p` VALUES ('P2210009', '259', '男', 19, 'cs', '9');
INSERT INTO `p` VALUES ('P2210010', '坤坤', '男', 20, 'honor', '10');
INSERT INTO `p` VALUES ('P2211105', '潘垠宇', '男', 19, 'genshin', '123456');

-- ----------------------------
-- Table structure for pv
-- ----------------------------
DROP TABLE IF EXISTS `pv`;
CREATE TABLE `pv`  (
  `PNO` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `WNO` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `VALUE` int NOT NULL,
  PRIMARY KEY (`PNO`, `WNO`) USING BTREE,
  INDEX `idx_scgrade`(`VALUE` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of pv
-- ----------------------------
INSERT INTO `pv` VALUES ('P2210001', 'W1', 0);
INSERT INTO `pv` VALUES ('P2210001', 'W2', 0);
INSERT INTO `pv` VALUES ('P2210002', 'W2', 0);
INSERT INTO `pv` VALUES ('P2210002', 'W3', 0);
INSERT INTO `pv` VALUES ('P2210002', 'W7', 0);
INSERT INTO `pv` VALUES ('P2210002', 'W9', 0);
INSERT INTO `pv` VALUES ('P2210002', 'WA', 0);
INSERT INTO `pv` VALUES ('P2210003', 'W1', 0);
INSERT INTO `pv` VALUES ('P2210003', 'W4', 0);
INSERT INTO `pv` VALUES ('P2210003', 'W6', 0);
INSERT INTO `pv` VALUES ('P2210003', 'W8', 0);
INSERT INTO `pv` VALUES ('P2210004', 'W5', 0);
INSERT INTO `pv` VALUES ('P2211105', 'W1', 0);
INSERT INTO `pv` VALUES ('P2211105', 'W2', 0);
INSERT INTO `pv` VALUES ('P2211105', 'W4', 0);
INSERT INTO `pv` VALUES ('P2211105', 'W6', 0);
INSERT INTO `pv` VALUES ('P2211105', 'W7', 0);
INSERT INTO `pv` VALUES ('P2211105', 'W8', 60);
INSERT INTO `pv` VALUES ('P2211105', 'W5', 99);

-- ----------------------------
-- Table structure for qishuivalue
-- ----------------------------
DROP TABLE IF EXISTS `qishuivalue`;
CREATE TABLE `qishuivalue`  (
  `PNO` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `VALUE` tinyint NOT NULL,
  PRIMARY KEY (`PNO`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of qishuivalue
-- ----------------------------
INSERT INTO `qishuivalue` VALUES ('P2210004', 0);
INSERT INTO `qishuivalue` VALUES ('P2211105', 99);

-- ----------------------------
-- Table structure for w
-- ----------------------------
DROP TABLE IF EXISTS `w`;
CREATE TABLE `w`  (
  `WNO` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `WNAME` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LEVEL` tinyint NOT NULL,
  `ELEMENT` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ANAME` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`WNO`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of w
-- ----------------------------
INSERT INTO `w` VALUES ('W1', '刺刀多普勒', 100, 'gold', 'cs');
INSERT INTO `w` VALUES ('W2', '可燃冰', 1, 'water', 'cs');
INSERT INTO `w` VALUES ('W3', '痛苦面具', 4, 'magic', 'honor');
INSERT INTO `w` VALUES ('W4', '爪刀', 4, 'fire', 'cs');
INSERT INTO `w` VALUES ('W5', '祁水', 4, 'gold', 'zmxy');
INSERT INTO `w` VALUES ('W6', '九齿钉耙', 6, 'gold', 'zmxy');
INSERT INTO `w` VALUES ('W7', '轮回杖', 4, 'gold', 'zmxy');
INSERT INTO `w` VALUES ('W8', '阿莫斯之弓', 4, 'gold', 'genshin');
INSERT INTO `w` VALUES ('W9', '和璞鸢', 4, 'gold', 'genshin');
INSERT INTO `w` VALUES ('WA', '天空之刃', 3, 'gold', 'genshin');

-- ----------------------------
-- View structure for pwv
-- ----------------------------
DROP VIEW IF EXISTS `pwv`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `pwv` AS select `p`.`PNO` AS `pno`,`p`.`PNAME` AS `pname`,`pv`.`VALUE` AS `value`,`w`.`WNAME` AS `WNAME`,`w`.`ANAME` AS `aname` from ((`p` join `pv`) join `w`) where ((`p`.`PNO` = `pv`.`PNO`) and (`w`.`WNO` = `pv`.`WNO`));

-- ----------------------------
-- Procedure structure for updatavalue
-- ----------------------------
DROP PROCEDURE IF EXISTS `updatavalue`;
delimiter ;;
CREATE PROCEDURE `updatavalue`(IN `New_PNO` char(10),
    IN `New_WNO` char(10),
    IN `New_VALUE` tinyint)
BEGIN
UPDATE pv
SET VALUE = New_VALUE
WHERE PNO = New_PNO AND WNO = New_WNO;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table pv
-- ----------------------------
DROP TRIGGER IF EXISTS `AddValue`;
delimiter ;;
CREATE TRIGGER `AddValue` BEFORE INSERT ON `pv` FOR EACH ROW BEGIN IF(
        new.WNO NOT IN(
            SELECT WNO
            FROM w
        )
    ) THEN
SET new.VALUE = 0;
END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table pv
-- ----------------------------
DROP TRIGGER IF EXISTS `AddQishui`;
delimiter ;;
CREATE TRIGGER `AddQishui` BEFORE INSERT ON `pv` FOR EACH ROW BEGIN IF(new.WNO = 'W5') THEN
INSERT INTO qishuivalue
VALUES(new.PNO, 0);
END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table pv
-- ----------------------------
DROP TRIGGER IF EXISTS `UpdataQishui`;
delimiter ;;
CREATE TRIGGER `UpdataQishui` AFTER UPDATE ON `pv` FOR EACH ROW BEGIN IF(new.WNO = 'W5') THEN
UPDATE qishuivalue
SET value = new.value
WHERE PNO = new.PNO;
END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table pv
-- ----------------------------
DROP TRIGGER IF EXISTS `SellQishui`;
delimiter ;;
CREATE TRIGGER `SellQishui` BEFORE DELETE ON `pv` FOR EACH ROW BEGIN IF(old.WNO = 'W5') THEN
DELETE FROM qishuivalue
WHERE PNO = old.PNO;
END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
