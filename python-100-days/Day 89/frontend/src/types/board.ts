export interface Board {
	id: number;
	name: string;
}

export interface BoardCreateForm extends Omit<Board, "id"> {}
export interface BoardUpdateForm extends Board {}
