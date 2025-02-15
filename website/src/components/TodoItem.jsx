export default function TodoItem(props) {
  return (
    <>
      <h1 id="list-name">{props.name}</h1>
      <p>{props.task}</p>
    </>
  )
}