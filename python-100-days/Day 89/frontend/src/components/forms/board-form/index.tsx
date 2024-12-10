import {
	Box,
	Button,
	Flex,
	FormControl,
	FormErrorMessage,
	FormLabel,
	Heading,
	Input,
	VStack,
	useToast,
} from "@chakra-ui/react";
import { useFormik } from "formik";
import { useSelector } from "react-redux";
import { FormType } from "../../../enums";
import { useCreateBoardMutation, useUpdateBoardMutation } from "../../../redux/api/boardApi";
import { boardSelector } from "../../../redux/selectors";
import { Board, BoardCreateForm, BoardUpdateForm } from "../../../types/board";
import { showErrorToastWithText, showSuccesToast } from "../form.toast";

interface BoardFormProps {
	onClose: () => void;
	formType: FormType;
}

const BoardFormComponent = ({ onClose, formType }: BoardFormProps) => {
	const toast = useToast();
	const [createBoardMutatuon] = useCreateBoardMutation();
	const [updateBoardMutation] = useUpdateBoardMutation();
	const board = useSelector(boardSelector);

	const sumbitFuncs = {
		[FormType.NEW]: async (value: BoardCreateForm) => {
			try {
				await createBoardMutatuon(value).unwrap();
				showSuccesToast(toast, "Board created");
				onClose();
			} catch (error) {
				showErrorToastWithText(toast, "Board may already exist");
			}
		},
		[FormType.EDIT]: async (value: BoardUpdateForm) => {
			try {
				await updateBoardMutation(value).unwrap();
				showSuccesToast(toast, "Board updated");
				onClose();
			} catch (error) {
				showErrorToastWithText(toast, "Error while updating");
			}
		},
	};

	const formik = useFormik<BoardUpdateForm>({
		initialValues: (formType === FormType.EDIT ? board : { id: -1, name: "" }) as Board,
		onSubmit: (values) => {
			sumbitFuncs[formType](values);
		},
	});

	return (
		<Flex align="center" justify="center">
			<Box bg="white" p={3} rounded="md">
				<form onSubmit={formik.handleSubmit}>
					<VStack spacing={4} align="center">
						<Heading size={"md"} color="purple" textTransform={"uppercase"}>
							{formType === FormType.NEW ? "Create" : "Update"} board
						</Heading>
						<FormControl isInvalid={!!formik.errors.name && formik.touched.name}>
							<FormLabel htmlFor="name">Board name</FormLabel>
							<Input
								id="name"
								name="name"
								type="text"
								variant="filled"
								onChange={formik.handleChange}
								value={formik.values.name}
							/>
							<FormErrorMessage>{formik.errors.name}</FormErrorMessage>
						</FormControl>
						<Button
							type="submit"
							colorScheme="purple"
							width="fit-content"
							alignSelf={"center"}>
							{formType === FormType.NEW ? "Create" : "Update"}
						</Button>
					</VStack>
				</form>
			</Box>
		</Flex>
	);
};

export default BoardFormComponent;
