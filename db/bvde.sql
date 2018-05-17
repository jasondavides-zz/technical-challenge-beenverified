CREATE TABLE genres (
  id int,
  name varchar(64)
)
;
INSERT INTO genres (id, name) VALUES
  (1, 'Rock'),
  (2, 'Country'),
  (3, 'Rap'),
  (4, 'Classical'),
  (5, 'Indie Rock'),
  (6, 'Noise Rock'),
  (7, 'Latin Pop Rock'),
  (8, 'Classic Rock'),
  (9, 'Pop')
;
CREATE TABLE songs (
  artist varchar(1024),
  title varchar(1024),
  genre int,
  duration int
)
;
INSERT INTO songs (artist, title, genre, duration) VALUES
  ('424', 'Gala', 5, 189),
  ('Colornoise', 'Amalie', 6, 246),
  ('Los Waldners', 'Horacio', 7, 165),
  ('Beatles', 'Strawberry Fields Forever', 8, 245),
  ('Chubby Checker', 'The Twist', 9, 235),
  ('Santana', 'Smooth', 9, 167),
  ('Bobby Darin', 'Mack the Knife', 1, 245),
  ('LeAnn Rhimes', 'How Do I Live', 2, 237),
  ('LMFAO', 'Party Rock Anthem', 3, 189),
  ('The Black Eyed Peas', 'I Gotta Feeling', 3, 219),
  ('Los Del Rio', 'Macarena', 9, 159),
  ('Olivia Newton-John', 'Physical', 9, 195),
  ('Debby Boone', 'You Light Up My Life', 9, 245),
  ('Beatles', 'Hey Jude', 8, 162)
;

