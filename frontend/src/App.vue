<template>
  <q-layout>
    <q-page-container>
      <q-page padding>
        <q-btn label="Export JSON" @click="exportTree" />
        <q-btn label="Duplicate Tree" @click="saveTree" />
        <q-btn label="Load All Trees" @click="loadAllTrees" />
        <div style="margin-top: 16px;"></div>
        <div v-for="(tree, index) in trees" :key="index">
          <TagView :tag="tree" @update="updateTree(index, $event)" />
        </div>
        <pre>{{ exportData }}</pre>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import axios from "axios";
import TagView from "./components/TagView.vue";

export default {
  name: "App",
  components: { TagView },
  data() {
    return {
      trees: [],
      exportData: "",
    };
  },
  methods: {
    exportTree() {
      const cleanTrees = this.trees.map(this.cleanTree);
      this.exportData = JSON.stringify(cleanTrees, null, 2);
    },
    saveTree() {
      const cleanTree = this.cleanTree(this.trees[0]); // Save the first tree for now
      axios.post("http://localhost:8000/trees/", cleanTree).then(() => {
        this.loadAllTrees();
      });
    },
    loadAllTrees() {
      axios.get("http://localhost:8000/trees/get_all_trees/").then((response) => {
        this.trees = response.data;
      });
    },
    updateTree(index, updatedTree) {
      this.trees[index] = updatedTree;
      const cleanTree = this.cleanTree(updatedTree);
      axios.put(`http://localhost:8000/trees/${updatedTree.id}/`, cleanTree).then(() => {
        this.loadAllTrees();
      });
    },
    cleanTree(node) {
      // Recursive function to clean up the tree structure
      const result = { name: node.name };
      if (node.data) {
        result.data = node.data; // Only include "data" if it exists
      }
      if (node.children) {
        result.children = node.children.map(this.cleanTree);
      }
      return result;
    },
  },
  mounted() {
    this.loadAllTrees();
  },
};
</script>
