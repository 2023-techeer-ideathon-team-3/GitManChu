import { Box, Typography } from "@mui/material";

export default function InfoBox() {
    return (
        <Box sx={{mt: '80px', display: 'flex', justifyContent: 'center', flexDirection: 'column', alignItems: 'center'}}>
            <Typography maxWidth='400px'>
            “안녕하세요. 저는 라면스프🍜입니다.
            라면에 스프가 없으면 제 역할을 못하는 것 처럼
            저도 회사에 꼭 필요한 인재가 되겠습니다”
            </Typography>
        </Box>
    )
}