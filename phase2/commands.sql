SELECT g_name AS guild_name, g_level AS guild_level
FROM guild
ORDER BY g_level DESC;

SELECT g.g_name AS guild_name, g.g_members AS member_count
FROM guild g
ORDER BY g.g_members DESC;

SELECT p.p_name AS player_name, s.s_kills AS total_kills
FROM player p
JOIN skywars s ON p.p_uuid = s.s_gameUUID
ORDER BY s.s_kills DESC;

-- insert upon guild creation / first time a corresponding player is looked up?
INSERT INTO guild (g_name, g_uuid, g_members, g_level, g_creationdate, g_tag)
VALUES ('TrollelLOL', '38473', 8, 9, '2015-07-15', ' ');

-- finding all data related to a player, in this case Lisa1051
SELECT
    p.p_name AS player_name,
    p.p_rank AS player_rank,
    p.p_joindate AS player_join_date,
    p.p_level AS player_level,
    g.g_name AS guild_name,
    g.g_members AS guild_members,
    g.g_level AS guild_level,
    g.g_creationdate AS guild_creation_date,
    g.g_tag AS guild_tag
FROM player p
LEFT JOIN guild g ON p.p_uuid = g.g_uuid
WHERE p.p_name = 'pasta';


-- Listing all pets owned by a player : someone is looking up the pet data

SELECT pt.pt_name AS pet_name, pt.pt_level AS pet_level
FROM pets pt
JOIN player p ON pt.pt_owner = p.p_uuid
WHERE p.p_name = 'pasta';

-- K/D ratio for a player in bedwars
-- note: don't know if this is handled by some other piece of code

SELECT 
    b.b_kills AS kills,
    b.b_deaths AS deaths,
    (CASE 
        WHEN b.b_deaths > 0 THEN CAST(b.b_kills AS DECIMAL(5,2)) / CAST(b.b_deaths AS DECIMAL(5,2))
        ELSE b.b_kills
     END) AS kd_ratio
FROM bedwars b
JOIN player p ON b.b_gameUUID = p.p_uuid
WHERE p.p_name = 'pasta';

-- Listing all friends of a player
SELECT p.p_name AS player_name, f.f_friend AS friend_name
FROM player p
JOIN friends f ON p.p_uuid = f.f_player
WHERE p.p_name = 'pasta';


-- Listing all punishments for a player
SELECT p.p_name AS player_name, pu.pu_type AS punishment_type, pu.pu_duration AS punishment_duration
FROM player p
JOIN punishments pu ON p.p_uuid = pu.pu_player
WHERE p.p_name = 'pasta';

-- Listing all bans for a player
SELECT p.p_name AS player_name, pu.pu_type AS punishment_type, pu.pu_duration AS punishment_duration
FROM player p
JOIN punishments pu ON p.p_uuid = pu.pu_player
WHERE p.p_name = 'pasta'
AND pu.pu_type = 'ban';


-- Listing all mutes for a player
SELECT p.p_name AS player_name, pu.pu_type AS punishment_type, pu.pu_duration AS punishment_duration
FROM player p
JOIN punishments pu ON p.p_uuid = pu.pu_player
WHERE p.p_name = 'pasta'
AND pu.pu_type = 'mute';


-- Listing all warnings for a player
SELECT p.p_name AS player_name, pu.pu_type AS punishment_type, pu.pu_duration AS punishment_duration
FROM player p
JOIN punishments pu ON p.p_uuid = pu.pu_player
WHERE p.p_name = 'pasta'
AND pu.pu_type = 'warn';


-- Listing average stats for skywars
SELECT 
    AVG(s.s_kills) AS average_kills,
    AVG(s.s_deaths) AS average_deaths,
    AVG(s.s_wins) AS average_wins,
    AVG(s.s_coins) AS average_coins,
    AVG(s.s_level) AS average_level,
    AVG(s.s_prestige) AS average_prestige
FROM skywars s;

-- Listing average stats for bedwars
SELECT 
    AVG(b.b_kills) AS average_kills,
    AVG(b.b_deaths) AS average_deaths,
    AVG(b.b_wins) AS average_wins,
    AVG(b.b_coins) AS average_coins,
    AVG(b.b_level) AS average_level,
    AVG(b.b_prestige) AS average_prestige
FROM bedwars b;

-- Listing average stats for duels

SELECT 
    AVG(d.d_kills) AS average_kills,
    AVG(d.d_deaths) AS average_deaths,
    AVG(d.d_wins) AS average_wins,
    AVG(d.d_coins) AS average_coins,
    AVG(d.d_level) AS average_level,
    AVG(d.d_prestige) AS average_prestige
FROM duels d;

-- Listing average ban time for all punishments
SELECT 
    AVG(pu.pu_duration) AS average_ban_time
FROM punishments pu
WHERE pu.pu_type = 'ban';

-- Listing average mute time for all punishments
SELECT 
    AVG(pu.pu_duration) AS average_mute_time
FROM punishments pu;


-- Finding ban counts across all players
SELECT 
    COUNT(pu.pu_type) AS ban_count
FROM punishments pu;

-- Finding mute counts across all players
SELECT 
    COUNT(pu.pu_type) AS mute_count
FROM punishments pu;



-- Finding all players with a certain rank
SELECT p.p_name AS player_name, p.p_rank AS player_rank
FROM player p
WHERE p.p_rank = 'VIP';

-- Finding guilds with level 10 or higher
SELECT g.g_name AS guild_name, g.g_level AS guild_level
FROM guild g
WHERE g.g_level >= 10;

