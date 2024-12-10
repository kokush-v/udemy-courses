// store.ts
import { configureStore } from "@reduxjs/toolkit";
import { boardApi } from "./api/boardApi";
import { taskApi } from "./api/taskApi";
import boardSlice from "./slice/boardSlice";
import formSlice from "./slice/taskFormSlice";
import taskSlice from "./slice/taskSlice";

const store = configureStore({
	reducer: {
		[boardApi.reducerPath]: boardApi.reducer,
		[taskApi.reducerPath]: taskApi.reducer,
		taskSlice,
		boardSlice,
		formSlice,
	},
	middleware: (getDefaultMiddleware) =>
		getDefaultMiddleware({}).concat([boardApi.middleware, taskApi.middleware]),
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
