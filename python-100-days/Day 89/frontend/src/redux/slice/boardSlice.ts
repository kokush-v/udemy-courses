import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { APP_KEYS } from "../../consts";
import { Board } from "../../types/board";

interface AddBoardPayload {
	board: Board;
}

interface BoardInitialState {
	board: Board | null;
}

const initial: BoardInitialState = {
	board: null,
};
const boardSlice = createSlice({
	name: "board",
	initialState: initial,
	reducers: {
		setBoard: (state, { payload }: PayloadAction<AddBoardPayload>) => {
			localStorage.setItem(APP_KEYS.STORAGE_KEYS.BOARD_NAME, payload.board.name);
			state.board = payload.board;
		},
	},
});

export const { setBoard } = boardSlice.actions;

export default boardSlice.reducer;
