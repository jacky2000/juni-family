# 우리 블로그 (정적 사이트)

빌드 도구 없이 HTML, CSS, JS 파일만으로 만든 블로그입니다. 서버나 데이터베이스가 필요 없습니다.

## 폴더 구성
| 경로 | 역할 |
|---|---|
| `index.html` | 홈. 글 목록을 `assets/posts.js`에서 읽어 최신순으로 보여줌 |
| `about.html` | 소개. 정보를 다루는 원칙 |
| `posts/` | 글 하나당 HTML 파일 하나 |
| `posts/_template.html` | 새 글 템플릿 |
| `assets/style.css` | 디자인 (흰색 바탕, 형광 파랑 #00b4ff, 형광 초록 #2bff88) |
| `assets/posts.js` | 글 목록 데이터 |

## 지금 확인하는 법
`index.html`을 더블클릭하면 브라우저에서 열립니다.

## 새 글 쓰는 법
1. `posts/_template.html`을 복사해서 `posts/새-글-주소.html`로 저장합니다. 파일명은 영문 소문자와 하이픈을 권장합니다.
2. `{ }` 자리를 채웁니다. 주소와 비용은 조사 파일 값을 그대로 쓰고, 값마다 `확인`, `불확실`, `확인 못 함` 배지를 붙입니다.
3. `assets/posts.js`의 맨 위에 객체 한 줄을 추가합니다. `slug`는 파일명(확장자 제외)과 같아야 합니다.

```js
{
  slug: "새-글-주소",
  title: "글 제목",
  summary: "목록에 보일 한두 문장",
  date: "YYYY-MM-DD",
  tags: ["태그1", "태그2"]
}
```

## 검색·공유 설정
- 모든 페이지에 `description`, `canonical`, Open Graph(카카오톡·페이스북 미리보기), 트위터 카드, JSON-LD가 들어 있습니다.
- 공유 미리보기 이미지는 `assets/og-default.png`(1200×630)입니다. 글마다 다른 이미지를 쓰려면 해당 글의 `og:image`와 JSON-LD `image`를 바꾸세요.
- 새 글을 쓰면 `sitemap.xml`에 `<url>` 한 줄도 추가하세요.
- 공개 후 [Google Search Console](https://search.google.com/search-console)과 [네이버 서치어드바이저](https://searchadvisor.naver.com)에 사이트와 sitemap.xml을 등록해야 검색에 빨리 잡힙니다.
- 카카오톡 미리보기가 옛날 모습이면 [카카오 공유 디버거](https://developers.kakao.com/tool/debugger/sharing)에서 캐시를 지우세요.

## 이름 바꾸기
"우리 블로그"는 임시 이름입니다. `index.html`, `about.html`, `posts/*.html`에서 "우리 블로그"를 검색해서 바꾸세요. 바꿀 곳은 제목(`<title>`), 로고, 푸터입니다.

## 인터넷에 공개하는 법 (선택)
정적 파일이라 GitHub Pages, Netlify, Cloudflare Pages 같은 무료 호스팅에 폴더째 올리면 됩니다. 어디에 올릴지는 아직 정하지 않았습니다.

## 글 쓸 때 원칙
- 웹에서 찾은 정보만 씁니다. 못 찾은 값은 "확인 못 함"으로 적습니다.
- 출처 링크와 조사 날짜를 적습니다.
- 직접 가지 않은 곳은 후기처럼 쓰지 않습니다.
- 가족의 실제 키나 구성 같은 개인 정보는 공개 글에 쓰지 않습니다.
