/* eslint-disable no-empty */
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { APP_KEYS } from "../../consts";
import { Board, BoardCreateForm, BoardUpdateForm } from "../../types/board";
import { setBoard } from "../slice/boardSlice";
import { taskApi } from "./taskApi";

export const boardApi = createApi({
	reducerPath: "boardApi",
	baseQuery: fetchBaseQuery({
		baseUrl: APP_KEYS.BACKEND_FULL_URL,
	}),
	tagTypes: ["Board"],
	endpoints: (builder) => ({
		getBoard: builder.query<Board, string>({
			providesTags: ["Board"],
			query(name) {
				return {
					url: APP_KEYS.BACKEND_KEYS.BOARD.ROOT(name),
					credentials: "include",
				};
			},
			async onQueryStarted(_args, { dispatch, queryFulfilled }) {
				try {
					const { data } = await queryFulfilled;
					dispatch(setBoard({ board: data }));
					dispatch(taskApi.endpoints.getTasks.initiate(data.id));
				} catch (error) {}
			},
		}),

		createBoard: builder.mutation<Board, BoardCreateForm>({
			invalidatesTags: ["Board"],
			query(data) {
				return {
					url: APP_KEYS.BACKEND_KEYS.BOARD.CREATE,
					method: "POST",
					body: data,
				};
			},
			async onQueryStarted(_args, { dispatch, queryFulfilled }) {
				const { data } = await queryFulfilled;
				dispatch(boardApi.endpoints.getBoard.initiate(data.name, { forceRefetch: true }));
			},
		}),

		updateBoard: builder.mutation<Board, BoardUpdateForm>({
			invalidatesTags: ["Board"],
			query(data) {
				return {
					url: APP_KEYS.BACKEND_KEYS.BOARD.UPDATE,
					method: "PUT",
					body: data,
				};
			},
		}),
	}),
});

export const { useCreateBoardMutation, useUpdateBoardMutation, useLazyGetBoardQuery } = boardApi;
