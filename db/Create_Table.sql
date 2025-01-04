CREATE TABLE tree_node (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent_id INTEGER REFERENCES tree_node(id) ON DELETE CASCADE,
    data JSONB DEFAULT '{}'::JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add an index on parent_id for better query performance
CREATE INDEX idx_tree_node_parent_id ON tree_node (parent_id);

-- Add a GIN index on the JSONB column for efficient JSON queries
CREATE INDEX idx_tree_node_data ON tree_node USING GIN (data);

-- Ensure unique names for children under the same parent
CREATE UNIQUE INDEX idx_tree_node_unique_name ON tree_node (name, parent_id);