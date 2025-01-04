-- Insert root node
INSERT INTO tree_node (name, parent_id, data) VALUES 
('root', NULL, '{}'::JSONB);

-- Insert child nodes under the root
INSERT INTO tree_node (name, parent_id, data) VALUES 
('child1', (SELECT id FROM tree_node WHERE name = 'root'), '{}'::JSONB),
('child2', (SELECT id FROM tree_node WHERE name = 'root'), '{"data": "c2 World"}'::JSONB);

-- Insert child nodes under child1
INSERT INTO tree_node (name, parent_id, data) VALUES 
('child1-child1', (SELECT id FROM tree_node WHERE name = 'child1'), '{"data": "c1-c1 Hello"}'::JSONB),
('child1-child2', (SELECT id FROM tree_node WHERE name = 'child1'), '{"data": "c1-c2 JS"}'::JSONB);