import { RootState } from "./store";

export const boardSelector = (state: RootState) => state.boardSlice.board;
export const taskSelector = (state: RootState) => state.taskSlice.tasks;
export const taskFormSelector = (state: RootState) => state.formSlice;
