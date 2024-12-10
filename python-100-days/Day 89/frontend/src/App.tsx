import {
	Heading,
	Link,
	Modal,
	ModalContent,
	ModalOverlay,
	Spinner,
	useDisclosure,
} from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import Board from "./components/board/board-container";
import BoardFormComponent from "./components/forms/board-form";
import Header from "./components/header";
import { FormType } from "./enums";
import { useLazyGetBoardQuery } from "./redux/api/boardApi";
import { boardSelector } from "./redux/selectors";
import { getBoardName } from "./utils";

function App() {
	const { isOpen, onOpen, onClose } = useDisclosure();
	const [refetch, { isFetching, isLoading, isSuccess }] = useLazyGetBoardQuery();
	const boardId = useSelector(boardSelector)?.name || getBoardName();
	const [formType, setFormType] = useState<FormType>(FormType.NEW);

	useEffect(() => {
		if (boardId) {
			refetch(boardId);
		}
	}, [refetch, boardId]);

	return (
		<div className="app h-[100vh] bg-transparent">
			<Header setFormType={setFormType} refetch={refetch} modalOpen={onOpen} />
			{isFetching || isLoading ? (
				<div className="w-full h-full flex justify-center items-center">
					<Spinner size={"xl"} />
				</div>
			) : !isSuccess ? (
				<div className="mt-[10%]">
					<Heading textAlign={"center"}>Board may not exist or an error occurred.</Heading>
					<Heading textAlign={"center"}>
						You can{" "}
						<Link onClick={onOpen} color={"teal.700"}>
							crate one!
						</Link>
					</Heading>
				</div>
			) : (
				<Board />
			)}
			<Modal isOpen={isOpen} onClose={onClose}>
				<ModalOverlay />
				<ModalContent>
					<BoardFormComponent formType={formType} onClose={onClose} />
				</ModalContent>
			</Modal>
		</div>
	);
}

export default App;
