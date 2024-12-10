/* eslint-disable react-hooks/exhaustive-deps */
import { AddIcon, EditIcon, Search2Icon } from "@chakra-ui/icons";
import { HStack, Heading, IconButton, Input, InputGroup, InputLeftElement } from "@chakra-ui/react";
import { Kbd } from "@nextui-org/kbd";
import { useState } from "react";
import { APP_KEYS } from "../../consts";
import { FormType } from "../../enums";
import { getBoardName } from "../../utils";

interface HeaderProps {
	modalOpen: () => void;
	refetch: (boardName: string) => void;
	setFormType: (formType: FormType) => void;
}

const Header = ({ modalOpen, refetch, setFormType }: HeaderProps) => {
	const localStorageBoardName = getBoardName().toString();
	const [boardName, setBoardName] = useState<string>(localStorageBoardName);

	function sendGetBoardQuery(event: React.KeyboardEvent<HTMLInputElement>) {
		if (event.key === "Enter" && boardName !== localStorageBoardName) {
			refetch(boardName);
			localStorage.setItem(APP_KEYS.STORAGE_KEYS.BOARD_NAME, boardName);
		}
	}

	return (
		<header className="header flex items-center gap-6 py-3 px-[5em] top-0 sticky z-30">
			<Heading textAlign={"center"}>Board</Heading>
			<InputGroup border={"1px solid #a3a3a3"} className="p-2 rounded-lg">
				<InputLeftElement pointerEvents="none">
					<IconButton aria-label="" variant={""} icon={<Search2Icon color="#a3a3a3" />} />
				</InputLeftElement>
				<Input
					color={"black"}
					variant={"unstyled"}
					type="text"
					placeholder="Board ID"
					value={boardName}
					onChange={(e) => setBoardName(e.target.value)}
					onKeyDown={sendGetBoardQuery}
				/>
				<Kbd keys={["enter"]}>Enter</Kbd>
			</InputGroup>
			<HStack>
				<IconButton
					aria-label=""
					variant={""}
					icon={<AddIcon />}
					onClick={() => {
						modalOpen();
						setFormType(FormType.NEW);
					}}
				/>
				<IconButton
					aria-label=""
					variant={""}
					icon={<EditIcon />}
					onClick={() => {
						modalOpen();
						setFormType(FormType.EDIT);
					}}
				/>
			</HStack>
		</header>
	);
};

export default Header;
