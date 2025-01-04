<template>
  <div class="tag-view">
    <div class="tag-header">
      <q-btn
        flat
        dense
        round
        @click="toggleCollapse"
        :label="collapsed ? '>' : 'v'"
        class="add-child-btn"
      />
      <div v-if="editingName" class="tag-name">
        <q-input
          v-model="localTag.name"
          @keyup.enter="saveName"
          dense
          placeholder="Enter name"
        />
      </div>
      <div v-else @click="editName" class="tag-name">
        {{ localTag.name }}
      </div>
      <q-btn class="add-child-btn" label="Add Child" @click="addChild" dense />
    </div>

    <div v-if="!collapsed">
      <div v-if="localTag.children && localTag.children.length === 0">
        <div v-if="localTag.data && Object.keys(localTag.data).length > 0" class="data-padding">
          <!-- Show data if available -->
          <q-input
            v-model="localTag.data.data"
            dense
            label="Data"
            @keyup.enter="updateData"
          />
        </div>

        <!-- <q-btn class="add-child-btn" label="Add Child" @click="addChild" dense /> -->
      </div>
      <div v-else>
        <!-- <q-btn class="add-child-btn" label="Add Child" @click="addChild" dense /> -->
        <div
          v-for="(child, index) in localTag.children"
          :key="index"
          class="child"
        >
          <TagView :tag="child" @update="updateChild(index, $event)" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TagView",
  props: {
    tag: Object,
  },
  data() {
    return {
      localTag: JSON.parse(JSON.stringify(this.tag)),
      collapsed: false,
      editingName: false,
    };
  },
  methods: {
    toggleCollapse() {
      this.collapsed = !this.collapsed;
      console.log(this.localTag);
    },
    addChild() {
      if (!this.localTag.children) {
        this.localTag.children = [];
        delete this.localTag.data; // Remove "data" when adding children
      }
      this.localTag.children.push({
        name: "New Child",
        data: { data: "Data" },
      });
      this.$emit("update", this.localTag);
    },
    editName() {
      this.editingName = true;
    },
    saveName() {
      this.editingName = false;
      this.$emit("update", this.localTag);
    },
    updateChild(index, updatedChild) {
      this.localTag.children.splice(index, 1, updatedChild);
      this.$emit("update", this.localTag);
    },
    updateData() {
      this.$emit("update", this.localTag);
    },
  },
  watch: {
    tag: {
      handler(newTag) {
        this.localTag = JSON.parse(JSON.stringify(newTag));
      },
      deep: true,
    },
  },
};
</script>

<style>
.tag-view {
  margin-left: 1rem;
}

.tag-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.tag-name {
  background: #007bff;
  color: white;
  padding: 0.75rem 0.75rem;
  border-radius: 0.25rem;
  cursor: pointer;
  flex-grow: 1;
  margin-left: 5px;
  font-size: medium;
}

.add-child-btn {
  margin-left: 16px;
  margin-bottom: 16px;
  background-color: #bdbdbd !important; 
  color: black !important; 
  border-radius: 4px !important; 
  padding: 8px 16px !important;
  box-shadow: none !important;
  min-width: auto !important; 
  height: auto !important; 
}
.data-padding{
  padding-bottom: 10px;
}
</style>
